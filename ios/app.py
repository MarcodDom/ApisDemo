import requests
import json
import random 
import time

url = "https://iot-madv-2026-default-rtdb.firebaseio.com/sensores.json"

def get_sensores():
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

def simular_sensores():
    while True:
        data = {
            "temperatura":random.randint(0,100),
            "humedad":random.randint(0,100),
        }
        response = requests.put(url, data=json.dumps(data))
        print(response.status_code)
        print(response.text)
        time.sleep(2)

if __name__ == "__main__":
    simular_sensores()
