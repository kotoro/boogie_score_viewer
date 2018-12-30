from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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