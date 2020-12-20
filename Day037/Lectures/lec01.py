import requests
from os import environ
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": environ["PIXELA_TOKEN"],
    "username": "pullynnhah",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
