import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
print()

response = requests.get(url="http://api.open-notify.org/is-now.json")
print(response)
print(response.status_code)
