import os
from twilio.rest import Client

ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_TOKEN"]

TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
MY_NUMBER = os.environ["MY_NUMBER"]


class NotificationManager:
    def __init__(self, sid, token):
        self.client = Client(sid, token)

    def send_message(self, from_number, to_number, message):
        self.client.messages.create(body=message, from_=from_number, to=to_number)
