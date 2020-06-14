import requests
from time import sleep
import datetime


last_message_time = 0

while True:
    response = requests.get('http://127.0.0.1:5000/history',
                            params={'after': last_message_time})
    data = response.json()
    for message in data['messages']:
        beauty_time = datetime.datetime.fromtimestamp(message['time'])
        beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M:%S')
        print(beauty_time, message['username'])
        print(message['text'])
        print()
        last_message_time = message['time']

    sleep(1)