import requests

api_key = ""
city = "Fortaleza"
url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    city+"&appid="+api_key+"&units=metric"

response = requests.get(url)
json = response.json()

description = json.get('weather')[0].get('description')
temp_min = json.get('main').get('temp_min')
temp_max = json.get('main').get('temp_max')

print("Today's forecast is", description)
print("The minimun temperature is", temp_min)
print("The minimun temperature is", temp_max)
