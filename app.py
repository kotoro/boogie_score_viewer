from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.request import urlopen
from PIL import Image
from pyzbar.pyzbar import decode
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

engine = create_engine('sqlite:///C:\\Users\\Djaurrey\\Desktop\\Trucs Rpi\\boogie_score_viewer\\boogie.db', )
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = session.query_property()


class Users(Base):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.Text, nullable=False)
	prenom = db.Column(db.Text, nullable=False)
	barcode = db.Column(db.Text, nullable=False)
	pseudo = db.Column(db.Text)
	score = db.Column(db.Integer, default=0)

class Drinks(Base):
	__tablename__ = 'drinks'
	id = db.Column(db.Integer, primary_key=True)
	userId = db.Column(db.Integer, nullable=False)
	type = db.Column(db.Integer, nullable=False)
	newCup = db.Column(db.Boolean, nullable=False)
	time = db.Column(db.DateTime, nullable=False)


@app.route('/launch_anim_scoreboard')
def launchAnim():
    socketio.emit('launch_anim_scoreboard')
    return "ok"

@app.route('/')
def index():
    return render_template("index.html")
	
@app.route('/test-codebarre')
def testcode():
	return render_template("codebarretest.html")
	
@app.route("/json/top_10")
def top10():
	user_list = list()
	for user in session.query(Users).order_by(Users.score.desc()).limit(10):
		user_list.append({'nom': user.nom, 'prenom': user.prenom})
	return jsonify(user_list)
	
@app.route("/json/classement_full")
def classementFull():
	user_list = list()
	for user in session.query(Users).order_by(Users.score.desc()).all():
		user_list.append({'nom': user.nom, 'prenom': user.prenom})
	return jsonify(user_list)
	
@app.route("/json/user_stats/<int:user_id>")
def userStats(user_id):
	user = session.query(Users).filter(Users.id == user_id).first()
	user_drinks = session.query(Drinks).filter(Drinks.userId == user_id).all()
	nb_drinks = 0
	nb_alc = 0
	nb_soft = 0
	cup_used = 1
	for drink in user_drinks:
		if drink.type == 4:
			nb_soft += 1
		else:
			nb_alc += 1
		if drink.newCup == True:
			cup_used += 1
		nb_drinks += 1
	score = int((nb_drinks * 10) + 100 * ((nb_drinks - cup_used) / nb_drinks))
	return jsonify({'nom': user.nom,
					'prenom': user.prenom, 
					'score': score,
					'nb_soft': nb_soft, 
					'nb_alc': nb_alc, 
					'nb_drinks': nb_drinks, 
					'cup_used': cup_used})

@app.route("/testdrink")
def testDrink():
	return render_template("test_drink.html")
	
@socketio.on("new_drink")
def addDrink(data):
	new_cup = False
	if (data['new_cup'] == "True"):
		new_cup = True
	session.add(Drinks(userId=data['user_id'], type=data['type'], newCup=new_cup, time=datetime.datetime.now()))
	session.query(Users).filter(Users.id == data['user_id']).first().score += 1
	session.commit()
	
@socketio.on("init_scan")
def sendScanData():
	url_portable = ""
	bar_data = decode(Image.open(urlopen(url_portable)))
	user = session.query(Users).filter(Users.barcode == bar_data[0][0]).first()
	user_stat = userStats(user.id)
	socketio.emit("mission-initialized", user_stat)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')