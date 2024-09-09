import requests
from datetime import datetime
import os

WEIGHT = 54
HEIGHT = 170
AGE = 21

APP_ID = "********"
API_KEY = "*********************"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/***********************/myWorkouts/workouts"

exercise_text = input("What exercise you did today? ")

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

date = datetime.now().strftime("%d%m%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_header = {
    "Authorization": "Bearer **************"
}
sheet_response = requests.post(sheety_endpoint, json=sheet_input,headers=bearer_header)
print(sheet_response.text)