import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/3.0/onecall?"
API_KEY = "f5b94f910d6c3cc82963a47ce30d88e3"
# f5b94f910d6c3cc82963a47ce30d88e3
CITY = "London"
url = BASE_URL + "appid=" + API_KEY + "&q="+ CITY

response = requests.get(url).json()

print(response)
