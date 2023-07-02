import requests
from datetime import datetime
import os
USERNAME = "danielgreenhalgh1995"
TOKEN = os.environ.get("pixela_token")
print(TOKEN)

pixela_URL = "https://pixe.la/v1/users"
PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#creates a user
#response = requests.post(url=URL, json=PARAMS)

# graphendpoint = f"{pixela_URL}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph3",
#     "name": "synsused",
#     "unit": "Syns",
#     "type": "int",
#     "color": "sora",
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#creates the graph
# response = requests.post(url=graphendpoint, json=graph_config, headers=headers)

pixelendpoint = f"{pixela_URL}/{USERNAME}/graphs/graph3"

today = datetime.now()
yesterday = datetime(year=2023, month=7, day=1)
print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "40",
}
#creates a pixel
response = requests.post(url=pixelendpoint, json=pixel_config, headers=headers)

update_pixel = f"{pixela_URL}/{USERNAME}/graphs/graph3/{yesterday.strftime('%Y%m%d')}"

updated_pixel_config = {
    "quantity": "20"
}

#update a pixel

#response = requests.put(url=update_pixel, json=updated_pixel_config, headers=headers)

# delete a pixel



delete_pixel = f"{pixela_URL}/{USERNAME}/graphs/graph3/{yesterday.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_pixel, headers=headers)

print(response.text)