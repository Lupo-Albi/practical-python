import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('There are', json.get('number'), 'people currently in space. They are:')

for person in json['people']:
    print(person['name'])
