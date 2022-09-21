

import requests
import json

API_KEY = "784188a5fa36dfccd4925e1f0cd8886a"

"http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"

# def get_response(api_key: str, city_name: str) -> json.JSONDecoder:
#     url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_key}"

#     return requests.get(url).json()