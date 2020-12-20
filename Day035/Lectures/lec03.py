from twilio.rest import Client
import sys

account_sid = sys.argv[1]
auth_token = sys.argv[2]
client = Client(account_sid, auth_token)

twilio_number = sys.argv[3]
my_number = sys.argv[4]

message = client.messages.create(
    body="This message was send from Python!!!",
    from_=twilio_number,
    to=my_number
)

print(message.status)
