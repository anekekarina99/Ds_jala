import requests
import json

url = 'http://localhost:5000/predict_abw'

data = {"abd_daya": 5,"sum_sample_g" : 8}

response = requests.post(url, json=data)
print(response.json())
