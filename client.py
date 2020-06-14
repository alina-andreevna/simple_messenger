from pprint import pprint
import requests

response = requests.get('http://127.0.0.1:5000/status')
pprint(response.json())

response = requests.get('http://127.0.0.1:5000/history')
pprint(response.json())

response = requests.post('http://127.0.0.1:5000/send', json={'username': 'nick', 'text': 'Hi everybody!'})
pprint(response.json())

response = requests.get('http://127.0.0.1:5000/history')
pprint(response.json())