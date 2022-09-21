import requests
import urllib.parse

API_KEY = "AIzaSyBDaeWicvigtP9xPv919E-RNoxfvC-Hqik"

base_uri = "https://maps.googleapis.com/maps/api/geocode/json?"

query = input("Input the place name: ")

url = base_uri + urllib.parse.urlencode({"address": query, "key": API_KEY})

response = requests.get(url=url).json()

print(response)
