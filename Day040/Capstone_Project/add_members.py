import os

import requests

ENDPOINT = 'https://api.sheety.co/0599c004d034001f75a8249650a83978/flightDeals/users'
TOKEN = os.environ['SHEETY_TOKEN']

print("Welcome to Paula's Flight Club.")
print('We find the best flight deals and mail you.')
first_name = input('What is your first name? ').title()
last_name = input('What is your last name? ').title()
while True:
    email = input('What is your email? ').lower()
    email_verification = input('Please, reenter your email: ').lower()
    if email == email_verification:
        break

users = {'user': dict(firstName=first_name, lastName=last_name, email=email)}
headers = dict(Authorization=f'Bearer {TOKEN}')
requests.post(url=ENDPOINT, json=users, headers=headers)

print("You're in the club!")
