# PLEASE FIX BUG (time)

"""
A brief showcase of the common use of 
the OpenWeatherMap API
Query for weather data
"""

import pytz
from datetime import datetime
import requests
from geopy.geocoders import Nominatim  # to get geolocation of places
from datetime import datetime as dt
import pytz  # to get timezone of places
from rich import print as rprint

API_KEY = "784188a5fa36dfccd4925e1f0cd8886a"

#######################################

# ask for the place whose data have to be retrieved
place = input("Input a city/state/country: ").lower()


# then we get the geolocation of that place using
# an OpenStreetMap Nominatim client from the `geopy` module

# instantiate a new Nominatim client
app = Nominatim(user_agent="geolocator")
# get the actual geolocation
location = app.geocode(place).raw
loc_lat = location["lat"]
loc_lon = location["lon"]

print(location['display_name'])

# then we query the OWM API


# don't know how I missed this but we can actually use the same
# OWM API to seach for geographical coordinates of the location




def get_response(api_key: str, lat: float, lon: float) -> dict:
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={api_key}"

    return requests.get(url).json()


res = get_response(API_KEY, loc_lat, loc_lon)
# rprint(f"""Place: {location['display_name']}
# Weather: {res['weather'][0]['description']}
# Temperature: {round(res['main']['temp'])} degrees C
# Wind Speed: {round(float(res['wind']['speed']) * 3600 / 1000, 1)} kmh
# Pressure: {res['main']['pressure']} hPa
# Humidity: {res['main']['humidity']} %""")

rprint(res)

# dt.now(pytz.timezone(res['timezone'])).strftime('%Y:%m:%d %H:%M:%S %z (UTC)')

# tz = pytz.timezone('CST6CDT')
# datetz = tz.localize(datetime(2020, 11, 17, 1, 37, 50), is_dst=None)
# print(datetz)

# tz = pytz.timezone('CST')
# print(tz)
# datetz = tz.localize(dt.fromtimestamp(res['dt']), is_dst=None)
# print(datetz)
