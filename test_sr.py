import requests
import json

url = 'http://localhost:5000/predict_sr'
data = {"average_weight": 5}

response = requests.post(url, json=data)
print(response.json())
