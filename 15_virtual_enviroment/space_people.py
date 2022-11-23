# Create venv with python3 -m venv venv_name
# Use with source venv_name/bin/activate
# Stop using it with deactivate

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('There are', json.get('number'), 'people currently in space. They are:')

for person in json['people']:
    print(person['name'])
