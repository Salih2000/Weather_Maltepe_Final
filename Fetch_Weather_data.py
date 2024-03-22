import requests
import json
from datetime import datetime

api_key = "gYwDa7AQnZ5DmHBWghIoX1hsR69hBrwD"
city_name = "Maltepe"

def get_current_weather(api_key, location_key):
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
    params = {
        "apikey": api_key,
        "details": True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        current_data = response.json()[0]
        current_data["RetrievedDateTime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        weather_data = {
            "Temperature": current_data['Temperature']['Metric']['Value'],
            "Weather Condition": current_data['WeatherText'],
            "Relative Humidity": current_data['RelativeHumidity'],
            "Wind Speed": current_data['Wind']['Speed']['Metric']['Value'],
            "Wind Direction": current_data['Wind']['Direction']['Localized']
        }
        return weather_data
    else:
        print("Error:", response.status_code)
        return None

def get_location_key(api_key, city_name):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": api_key,
        "q": city_name
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            location_key = data[0]["Key"]
            return location_key
    print("Error: Location key not found")
    return None
