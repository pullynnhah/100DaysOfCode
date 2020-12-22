import os
import smtplib
from twilio.rest import Client

ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_TOKEN"]

TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
MY_NUMBER = os.environ["MY_NUMBER"]

EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_EMAIL_PASSWORD"]


class NotificationManager:
    def __init__(self, email=None, password=None):
        self.client = None
        self.email = email
        self.password = password

    def send_message(self, from_number, to_number, message, sid, token):
        self.client = Client(sid, token)
        self.client.messages.create(body=message, from_=from_number, to=to_number)

    def send_email(self, message, *emails):
        emails = ', '.join(emails)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email, to_addrs=emails, msg=message)
