import json
import requests

# Read data.json file
with open('data.json') as f:
    data = json.load(f)

    for entity in data:
        response = requests.post(url='http://localhost:1026/ngsi-ld/v1/entities', 
                                 headers={"content-type": "application/json"},  
                                 data=json.dumps(entity))
        print(response.status_code)