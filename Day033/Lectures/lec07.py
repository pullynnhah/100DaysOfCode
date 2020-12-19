import requests
from datetime import datetime

LATITUDE = -22.338930
LONGITUDE = -49.055190
URL = "https://api.sunrise-sunset.org/json"


def hour_time(time):
    return int(time.split("T")[1].split(':')[0])

parameters = {
    'lat': LATITUDE,
    'lng': LONGITUDE,
    'formatted': 0
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

data = response.json()
print(data)
print()


sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
print()

time_now = datetime.now()
print(time_now)
print()

sunrise_hour = hour_time(sunrise)
sunset_hour = hour_time(sunset)
now_hour = time_now.hour

if sunrise_hour <= now_hour <= sunset_hour:
    print("It's day time!")
else:
    print("It's night time!")
