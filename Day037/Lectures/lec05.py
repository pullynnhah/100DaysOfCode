import requests
from os import environ

USERNAME = "pullynnhah"
TOKEN = environ["PIXELA_TOKEN"]
GRAPH_ID = "graph"
delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20201220"


headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
