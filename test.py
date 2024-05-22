import requests

# Function to get all engines linked to an aircraft
def get_engines_linked_to_aircraft(aircraft_id):
    # Define the Context Broker URL for the aircraft entity
    url_aircraft = f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Aircraft:{aircraft_id}'
    
    # Set the headers
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }
    
    # Make the GET request to retrieve the aircraft entity
    response_aircraft = requests.get(url_aircraft, headers=headers)
    
    # Check if the request was successful
    if response_aircraft.status_code == 200:
        # Parse the JSON response
        aircraft_data = response_aircraft.json()
        
        # Check if 'hasEngine' is a list or a single relationship
        has_engine = aircraft_data.get('hasEngine')
        engine_ids = []
        
        if isinstance(has_engine.get('value'), list):
            # Multiple engines case
            engine_ids = [engine['object'] for engine in has_engine['value']]
        else:
            # Single engine case
            engine_ids = [has_engine['object']]
        
        # Retrieve each engine entity
        engines = []
        for engine_id in engine_ids:
            # Define the Context Broker URL for the engine entity
            url_engine = f'http://localhost:1026/ngsi-ld/v1/entities/{engine_id}'
            
            # Make the GET request to retrieve the engine entity
            response_engine = requests.get(url_engine, headers=headers)
            
            if response_engine.status_code == 200:
                engine_data = response_engine.json()
                engines.append(engine_data)
            else:
                print(f"Error retrieving engine {engine_id}: {response_engine.status_code}")
                print(response_engine.text)
        return engines
    else:
        print(f"Error retrieving aircraft {aircraft_id}: {response_aircraft.status_code}")
        print(response_aircraft.text)
        return None

# Function to get vibration data for a specific engine
def get_engine_data(engine_id):
    # Define the Context Broker URL
    url = 'http://localhost:1026/ngsi-ld/v1/entities'
    
    # Define the query parameter with proper syntax
    query = f'isSensorOf=="{engine_id}"'
    
    # Set the headers
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }
    
    # Make the GET request to retrieve the vibration data
    response = requests.get(url, params={'q': query}, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        response = response.json()
        
        # Check if the response is not empty
        if response:
            return response
        else:
            print("No vibration data found for engine:", engine_id)
            return None
    else:
        print(f"Error retrieving vibration data for engine {engine_id}: {response.status_code}")
        print(response.text)
        return None

# Example usage
aircraft_id = '001'  # Replace with the actual aircraft ID
engine_data = get_engines_linked_to_aircraft(aircraft_id)


if engine_data:
    for engine in engine_data:
        engine_id = engine['id']#.split(':')[-1]  # Extract the engine ID from the URN
        print(engine_id)
        print(get_engine_data(engine_id))
