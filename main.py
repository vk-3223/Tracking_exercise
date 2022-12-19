from email import header
from unittest import result
from datetime import datetime
import requests
import os

api_id = os.environ["6ea856cb"]
api_key = os.environ["781f10b0c32581577fe072d8ecf4e043"]

exercies_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercies_text = input("tell me which exercies ")
sheety_endpoint = os.environ["https://api.sheety.co/7e38f13a20b614d2e8d6f1cc4c9029ad/workoutTracking/workouts"]
header ={
    "x-app-id":api_id,
    "x-app-key":api_key,
}

parameters = {
    "query":exercies_text,
    "gender":"male",
    "weight_kg":56,
    "height_cm":156,
    "age":19
}

response = requests.post(url=exercies_endpoint,json=parameters,headers=header)
result = response.json()

today_time = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
headers = {
    "Authorization":"Basic dmVuaWw6VmtodW50QEA="
}
for exerice in result["exercises"]:
    sheet_input = {
        "workout":{
            "date":today_time,
            "time":now_time,
            "exercise":exerice["name"].title(),
            "duration":exerice["duration_min"],
            "calories":exerice["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint,json=sheet_input,headers=headers)
print(sheet_response.text)
