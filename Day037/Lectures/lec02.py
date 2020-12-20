import requests
from os import environ

USERNAME = "pullynnhah"
TOKEN = environ["PIXELA_TOKEN"]
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "graph",
    "name": "100 Days Of Code",
    "unit": "days",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
