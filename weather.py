import urllib
import json
from voice import talking
import config


def get_zip():
    url = 'http://ipinfo.io/json'
    f = urllib.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    my_zip = parsed_json['postal']
    city = parsed_json['city']
    state = parsed_json['region']
    data = [my_zip, city, state]
    return data


def current_weather():
    key = config.wunder_key
    while True:
        my_zip = get_zip()
        text = 'getting weather information on ' + my_zip[1] + ',' + my_zip[2]
        talking(text)
        url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + my_zip[0] + '.json'
        try:
            f = urllib.urlopen(url)
        except IOError:
            print IOError
            talking('You are not connected to the internet')
            break
        json_string = f.read()
        parsed_json = json.loads(json_string)
        city = parsed_json['location']['city']
        weather = parsed_json['current_observation']['weather']
        temperature_string = parsed_json['current_observation']['temp_f']
        temperature_string = str(temperature_string)
        feels_like_string = parsed_json['current_observation']['feelslike_f']
        weather_text = 'Weather in ' + city + ': ' + weather.lower() + '. The temperature is ' + temperature_string + \
                       ' and feels like ' + feels_like_string + '.'
        talking(weather_text)
        f.close()
        break


def forecast():
    key = config.wunder_key
    while True:
        my_zip = get_zip()
        text = 'getting weather information on ' + my_zip[1] + ',' + my_zip[2]
        talking(text)
        url = 'http://api.wunderground.com/api/' + key + '/geolookup/forecast/q/' + my_zip[0] + '.json'
        try:
            f = urllib.urlopen(url)
        except IOError:
            print IOError
            talking('You are not connected to the internet')
            break
        json_string = f.read()
        parsed_json = json.loads(json_string)
        for day in parsed_json['forecast']['simpleforecast']['forecastday']:
            x = day['date']['day']
            y = str(x)
            forecast_text = 'The weather for ' + day['date']['weekday'] + ', ' + day['date']['monthname'] + ' ' + y + \
                            ' will be ' + day['conditions'] + ' with a high of ' + day['high'][
                                'fahrenheit'] + ' degrees fahrenheit and a low of ' + day['low'][
                                'fahrenheit'] + ' degrees ferinheight'
            talking(forecast_text)
        f.close()
        break
