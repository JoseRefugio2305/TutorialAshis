from logging import debug
import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY']='secret'
socketiocon = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketiocon.on('message')
def handleMessage(msg, id):
    print("El mensaje enviado es: "+msg+" enviado por el usuario: "+str(id))
    send(msg, to=id)

@socketiocon.on('join')
def on_join(data):
    username = 'jose'
    room = data["room"]
    print(data["room"])
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketiocon.on('leave')
def leave(room):
    username='jose'
    print("leave")
    leave_room(room['room'])
    send(username+" abandono la habitacion", to=room['room'])

if __name__=='__main__':
    socketiocon.run(app, debug=True)
    #socketiocon.run(app,  port=int(os.environ.get('PORT', 5000)))