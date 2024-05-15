import requests

# Define the Context Broker URL
url = 'http://localhost:1026/ngsi-ld/v1/entities'

# Define the engine_id
engine_id = '001'  # Update this with your actual engine_id value

# Define the query parameter
query = f'isSensorOf=="urn:ngsi-ld:Engine:{engine_id}"'

# Set the headers
headers = {
    'Accept': 'application/ld+json',
    'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
}

# Make the GET request
response = requests.get(url, params={'q': query}, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    entities = response.json()
    
    # Print the entities
    for entity in entities:
        print(entity)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
