import requests
import os

LATITUDE = -22.338930
LONGITUDE = -49.055190

api_key = os.environ["OWM_API_KEY"]
api_url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(api_url, params=params)
response.raise_for_status()

data = response.json()

for hourly_data in data["hourly"][:12]:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 700:
        print("Bring an umbrella.")
        break
