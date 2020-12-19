import requests

params = {
    "amount": 10,
    "type": "boolean"
}

url = "https://opentdb.com/api.php"

response = requests.get(url=url, params=params)
response.raise_for_status()
question_data = response.json()['results']
