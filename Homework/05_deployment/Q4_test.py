import requests

url = "http://192.168.0.133:9696/predict"

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
result = requests.post(url, json=client).json()

print(result)


# Probability of getting a credit (Flask)
# 0.1396