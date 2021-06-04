from flask import Flask, render_template
from flask_sockets import Sockets
import time

app = Flask(__name__)
sockets = Sockets(app)

def on_message(self, message):
    if message == 'hello':
        self.send('Вы поздоровались')
    elif message == 'bye':
        self.send('Вы попрощались')
    else:
        self.send('Я не знаю такой команды')

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        print(ws)
        print(message)
        on_message(ws,message)
        

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
