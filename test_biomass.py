import requests
import json

url = 'http://localhost:5000/predict_abw'

data = {"total_seed": 5,"area" : 8}

response = requests.post(url, json=data)
print(response.json())