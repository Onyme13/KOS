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

"""[{'id': 'urn:ngsi-ld:vibration:001', 'type': 'Vibration', 
'isSensorOf': {'type': 'Relationship', 'object': 'urn:ngsi-ld:Engine:001'}, 
'vibrationTime': {'type': 'Property', 'value': '2020-01-01T00:00:00Z'}, 
'vibrationUnit': {'type': 'Property', 'value': 'm/s2'}, 
'vibrationValue': {'type': 'Property', 'value': 0.5}}]"""


response = requests.get(url='http://localhost:1026/ngsi-ld/v1/entities?q=isSensorOf==urn:ngsi-ld:Engine:001')
print("\n\n\nGetting Vibration entities:\n")
print(response.json())


