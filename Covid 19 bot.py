import requests
from win10toast import ToastNotification
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text =f'"Confirmed Cases : {data["cases"]} \nDeath : {data["death"]} \nRecovered : {data["recovered"]}'

while True:
   toast = ToastNotifier()
   toast.show_toast("Covid-19 Updates",text,duration=20)
   time.sleep(60)

update()
