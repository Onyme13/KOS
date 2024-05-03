import requests

# Get Engine entities
response = requests.get(url='http://localhost:1026/ngsi-ld/v1/entities?type=Engine')
print("Getting Engine entities:\n")
print(response.json())


# Get Aircraft entities
response = requests.get(url='http://localhost:1026/ngsi-ld/v1/entities?type=Aircraft')
print("\n\n\nGetting Aircraft entities:\n")
print(response.json())

# Get maintenance entities (data)
response = requests.get(url='http://localhost:1026/ngsi-ld/v1/entities?type=Maintenance')
print("\n\n\nGetting Maintenance entities:\n")
print(response.json())


