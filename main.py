import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": "123sfdawetr",
    "username": "mike123mike",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{parameters['username']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# headers = {
#     "X-USER-TOKEN": parameters['token']
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#
# view_graph_endpoint = f"{pixela_endpoint}/{parameters['username']}/graphs/{graph_config['id']}.html"
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# pixel_add_endpoint = f"{pixela_endpoint}/{parameters['username']}/graphs/{graph_config['id']}"
#
today = datetime.datetime.today().strftime("%Y%m%d")
#
# pixel_config = {
#     "date": today,
#     "quantity": "9.74"
# }
#
# headers = {
#     "X-USER-TOKEN": parameters['token']
# }



# response = requests.post(url=pixel_add_endpoint, json=pixel_config, headers=headers)
# print(response.text)

delete_endpoint =f"{pixela_endpoint}/{parameters['username']}/graphs/{graph_config['id']}/{today}"

print(delete_endpoint)


headers = {
    "X-USER-TOKEN": parameters['token']
}


response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)



print(delete_endpoint)