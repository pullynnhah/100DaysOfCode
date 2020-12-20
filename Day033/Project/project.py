import os
import smtplib
import requests
from datetime import datetime
from time import sleep

LATITUDE = -22.338930
LONGITUDE = -49.055190
ISS_API = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}

email = os.environ["MY_EMAIL"]
password = os.environ["MY_EMAIL_PASSWORD"]


def check_coordinates():
    response = requests.get(url=ISS_API)
    response.raise_for_status()
    data = response.json()
    lat = float(data["iss_position"]["latitude"])
    long = float(data["iss_position"]["longitude"])

    return abs(LATITUDE - lat) <= 5 and abs(LONGITUDE - long) <= 5


def is_dark():
    response = requests.get(url=SUNRISE_SUNSET_API, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = datetime.now().hour
    return not (sunrise <= now_hour <= sunset)


def send_email(string):
    text = f'Subject: ISS Report\n\n{string}'
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=text)


while True:
    if check_coordinates() and is_dark():
        send_email('Look up!')
    sleep(60)
