import json
import requests

BASE_URL = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
#API_KEY = "f5b94f910d6c3cc82963a47ce30d88e3"
# f5b94f910d6c3cc82963a47ce30d88e3

#response = requests.get(BASE_URL).json()
response = requests.get(BASE_URL)

print(response.json([]))
