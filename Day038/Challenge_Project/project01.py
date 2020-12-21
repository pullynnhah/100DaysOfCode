import os

import requests
import json

API_ID = os.environ['NUTRITIONIX_API_ID']
API_KEY = os.environ['NUTRITIONIX_API_KEY']
END_POINT = ' https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = "female"
WEIGHT_KG = 72.3
HEIGHT_CM = 162
AGE = 24

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}

params = {
    'query': input('Tell me which exercise you did: '),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=END_POINT, json=params, headers=headers)
print(response.json())
