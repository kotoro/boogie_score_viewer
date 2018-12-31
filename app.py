from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


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

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')