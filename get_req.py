import requests


number = 5
url = "http://127.0.0.1:5000/results/testiot43/" + str(number)

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
