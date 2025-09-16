#  ---------- day - 38 ----------------
import requests

GENDER = "male"
WEIGHT = 72
HEIGHT = 172
AGE = 24

APP_ID = "1e639f9e"
APP_KEY = "b44be246d11f9a0d5a5014fa41dff229"
nutrionix_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)

