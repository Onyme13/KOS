import requests

# Function to get aircraft data and extract the engine ID
def get_engine_id_from_aircraft(airplane_id):
    # Define the Context Broker URL
    url = f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Aircraft:{airplane_id}'
    
    # Set the headers
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        aircraft_data = response.json()
        
        # Extract the engine ID
        engine_id = aircraft_data['hasEngine']['object']
        print("Engine ID:", engine_id)
        return engine_id
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Example usage
airplane_id = '001'  # Replace with the actual airplane ID
get_engine_id_from_aircraft(airplane_id)
