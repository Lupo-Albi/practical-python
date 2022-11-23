import requests


def get_weather():
    api_key = ""
    city = "Fortaleza"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid="+api_key+"&units=metric"

    response = requests.get(url)
    json = response.json()

    description = json.get('weather')[0].get('description')
    temp_min = json.get('main').get('temp_min')
    temp_max = json.get('main').get('temp_max')

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max
    }


def main():
    # Print the results
    weather_dict = get_weather()

    print("Today's forecast is", weather_dict.get('description'))
    print("The minimun temperature is", weather_dict.get('temp_min'))
    print("The minimun temperature is", weather_dict.get('temp_max'))


main()
