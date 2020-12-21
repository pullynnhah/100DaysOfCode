import os
import requests
from datetime import datetime

API_ID = os.environ['NUTRITIONIX_API_ID']
API_KEY = os.environ['NUTRITIONIX_API_KEY']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY = 'https://api.sheety.co/5103eb866c8b4c046d653d3a1082f182/myWorkouts/workouts'
GENDER = "female"
WEIGHT_KG = 72.3
HEIGHT_CM = 162
AGE = 24


def create_row(data):
    today = datetime.now()
    return {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": data["name"].title(),
        "duration": data["duration_min"],
        "calories": data["nf_calories"]
    }


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
exercises = response.json()["exercises"]
for exercise in exercises:
    task = dict(workout=create_row(exercise))
    headers = {"Authorization": f'Bearer {SHEETY_TOKEN}'}
    response = requests.post(SHEETY, json=task, headers=headers)
