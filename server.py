from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)

messages = [
    {'username': 'Jack', 'text': 'Hello!', 'time': time.time()},
    {'username': 'Mary', 'text': 'Hi, Jack.', 'time': time.time()}
]

users = {
    # username: password

    'Jack': 'black',
    'Mary': '12345'
}


# @app.route("/")
# def hello():
#     return "Hello world!"


@app.route("/status")
def status():
    return {'status': 'ok',
            'current time': datetime.now(),
            'users count': len(users),
            'users': users,
            'messages count': len(messages)
            }


@app.route("/history")
def history():
    after = float(request.args['after'])

    filtered_messages = [m for m in messages if after < m['time']]

    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send():
    # /***
    # request: {'username': str, 'text': str}
    # response: {'status: True}
    # ***/

    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']

    if username in users:
        real_password = users[username]
        if real_password != password:
            return {'ok': False}
    else:
        users[username] = password

    new_message = {'username': username, 'text': text, 'time': time.time()}
    messages.append(new_message)

    return {'ok': True}


app.run()
