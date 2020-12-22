import pandas
import random
import smtplib
import os
import datetime as dt


def get_letter(birthday_name):
    letter_filename = f'./letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(letter_filename) as file:
        letter = file.read()
    letter = letter.replace('[NAME]', birthday_name)
    return letter


now = dt.datetime.now()
today = (now.month, now.day)

data_frame = pandas.read_csv("birthdays.csv")
info = data_frame.to_dict(orient="records")

birthday_info = []
for person in info:
    birthday = (person['month'], person['day'])
    if birthday == today:
        birthday_info.append((person['name'], person['email']))

if len(birthday_info) != 0:

    my_email = os.environ["MY_EMAIL"]
    password = os.environ["MY_EMAIL_PASSWORD"]
    for person in birthday_info:
        name = person[0]
        email = person[1]

        message = f'Subject: Happy Birthday!!!\n\n{get_letter(name)}'
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)
