from twilio.rest import Client
import os

account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_TOKEN"]
client = Client(account_sid, auth_token)

twilio_number = os.environ["TWILIO_NUMBER"]
my_number = os.environ["MY_NUMBER"]

message = client.messages.create(
    body="This message was send from Python!!!",
    from_=twilio_number,
    to=my_number
)

print(message.status)
