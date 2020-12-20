import requests
from os import environ

USERNAME = "pullynnhah"
TOKEN = environ["PIXELA_TOKEN"]
GRAPH_ID = "graph"
update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20201220"

pixel_config = {
    "date": "20201220",
    "quantity": "3"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=update_endpoint, json=pixel_config, headers=headers)
print(response.text)
