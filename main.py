#  ---------- day - 38 ----------------
import requests
from datetime import datetime
# from requests.auth import HTTPBasicAuth
import os

GENDER = "YOUR GENDER"
WEIGHT = "YOUR WEIGHT"
HEIGHT = "YOUR HEIGHT"
AGE = "YOUR AGE"

APP_ID = os.environ["NT_APP_ID"]
APP_KEY = os.environ["NT_API_KEY"]
nutrionix_api = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api = os.environ["sheety_api"]

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}

parameters = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE,
}

exercise_response = requests.post(url=nutrionix_api, json=parameters, headers=headers)
result = exercise_response.json()
# print(result)

# ------------ write in sheety --------
today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%X")

bearer_headers = {
"Authorization": f"Bearer {os.environ['TOKEN']}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date" : DATE,
            "time" : TIME,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }

# sheet_response = requests.post(url=sheety_api, json=sheet_inputs)
# print(sheet_response.text)

#  ------------ Authentication ---------
#  ------ basic authentication ---------
# sheet_response = requests.post(url=sheety_api, json=sheet_inputs, auth=("username", "pass"))

# ------- Bearer authentication -----

    sheet_response = requests.post(sheety_api, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)



