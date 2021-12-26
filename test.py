import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "nutrition/30/M/PROTEIN")

print(str(response.content))