from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)
    
@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        print('Message from client: ' + message)
        if message == 'Bye':
            self.send('Вы попрощались')
        elif message == 'Hey':
            self.send('Вы поздоровались')
        else:
            self.send('Я не знаю такой команды')


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
