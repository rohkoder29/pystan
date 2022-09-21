import requests
from requests.structures import CaseInsensitiveDict
from rich import print as show

# Parameters

# categories -
# conditions -
# filter -
# bias -
# limit -
# offset -
# lang -
# name -
# apiKey -

# query = input('Input a place: ')

URL = "https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=1&apiKey=fcf8e6a23d494aaaa99f1a6ab320b23b"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(URL, headers=headers).json()

# show(resp['features'][0]['geometry']['coordinates'])
show(resp)
