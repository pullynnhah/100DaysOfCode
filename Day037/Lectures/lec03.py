import requests
import sys
from os import environ
from datetime import datetime

USERNAME = "pullynnhah"
TOKEN = environ["PIXELA_TOKEN"]
GRAPH_ID = "graph"
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
quantity = input("How many days did you complete today? ")

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
