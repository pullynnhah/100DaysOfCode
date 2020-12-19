import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
response = requests.get(url="http://api.open-notify.org/is-now.json")
response.raise_for_status()
