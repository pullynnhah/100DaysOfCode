import requests
from os import environ

USERNAME = "pullynnhah"
TOKEN = environ["PIXELA_TOKEN"]
GRAPH_ID = "graph"
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": "20201220",
    "quantity": "2"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
