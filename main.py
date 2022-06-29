import os

import requests
from datetime import datetime

TOKEN = os.environ['TOKEN']
USERNAME = os.environ['USERNAME']

today = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.0",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response)

