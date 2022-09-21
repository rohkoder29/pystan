"""
A brief showcase of the common use of 
the OpenWeatherMap API
using the OneCall mode version 2.5 and Developer subscription

Normally one uses "https://api.openweathermap.org" as endpoint
But having a Developer subscription, I can use "https://pro.openweathermap.org"

"""

import requests
from geopy.geocoders import Nominatim  # to get geolocation of places
from datetime import datetime as dt
import pytz  # to get timezone of places
from rich import print

API_KEY = "784188a5fa36dfccd4925e1f0cd8886a"

#######################################

# ask for the place whose data have to be retrieved
place = input("Input a city/state/country: ").lower()

# then we get the geolocation of that place using
# an OpenStreetMap Nominatim client from the geopy module

# instantiate a new Nominatim client
app = Nominatim(user_agent="geolocator")
# get the actual geolocation
location = app.geocode(place).raw
l_lat = location["lat"]
l_lon = location["lon"]

# optional entries
exclude = "minutely,hourly,daily,alerts"
lang = "fr"
# use units=metric to have temp in C and wind in m/s
units = "metric"

# then we query the OWM API


def get_weather(api_key: str, lat: float, lon: float) -> dict:
    url = f"https://pro.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&units={units}&lang={lang}&appid={api_key}"

    response = requests.get(url).json()  # data in JSON format
    return response
    
    # time = pytz.timezone(response["timezone"])
    # temp = response["current"]["temp"]
    # weather = response["current"]["weather"][0]["description"]
    # wind = response["current"]["wind_speed"]
    # pressure = response["current"]["pressure"]
    # humidity = response["current"]["humidity"]

    # return {
    #     "time": dt.now(time).strftime("%Y:%m:%d %H:%M:%S %z (UTC)"),
    #     "weather": weather,
    #     "temp": temp,
    #     "wind": wind,
    #     "pressure": pressure,
    #     "humidity": humidity,
    # }


loc_weather = get_weather(API_KEY, l_lat, l_lon)
# print(f"""Place: {location['display_name']}
# Time: {loc_weather['time']}
# Weather: {loc_weather['weather']}
# Temperature: {round(loc_weather['temp'], 2)} C
# Wind Speed: {loc_weather['wind']} m/s
# Pressure: {loc_weather['pressure']} hPa
# Humidity: {loc_weather['humidity']} %""")


print(loc_weather)
