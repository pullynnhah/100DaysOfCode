import smtplib
import random
import os
import datetime as dt

weekdays = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}


def random_quote():
    with open('quotes.txt') as file:
        quotes = file.readlines()
    return random.choice(quotes)


now = dt.datetime.now()
weekday = now.weekday()
check_weekday = input('Enter which day of the week do you want to send an email: ').lower()

if weekdays[check_weekday] == weekday:
    email = os.environ["MY_EMAIL"]
    password = os.environ["MY_EMAIL_PASSWORD"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        message = f'Subject: Motivational Quote\n\n{random_quote()}'
        connection.sendmail(from_addr=email, to_addrs=email, msg=message)
