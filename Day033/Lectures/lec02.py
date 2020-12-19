import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    print("Error")
else:
    print("No Error")
print()

response = requests.get(url="http://api.open-notify.org/is-now.json")

if response.status_code != 200:
    print("Error")
else:
    print("No Error")
