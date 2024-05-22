import requests

# Get all aircraft entities
def get_all_aircraft():
    # Define the Context Broker URL
    url = 'http://localhost:1026/ngsi-ld/v1/entities'
    
    # Define the query parameter to filter by type 'Aircraft'
    params = {
        'type': 'Aircraft'
    }
    
    # Set the headers
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }
    
    # Make the GET request
    response = requests.get(url, params=params, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the entities
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Get all engine entities
def get_all_engines():
    # Define the Context Broker URL
    url = 'http://localhost:1026/ngsi-ld/v1/entities'
    
    # Define the query parameter to filter by type 'Engine'
    params = {
        'type': 'Engine'
    }
    
    # Set the headers
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }
    
    # Make the GET request
    response = requests.get(url, params=params, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the entities
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
    



# Get aircraft data. Such as id, model, serial number.
def get_aircraft(airplane_id):
    aircraft = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:{airplane_id}')
    response = aircraft.json()
    #aircraft_id = response['id']
    #model = response['aircraftModel']['value']
    #serial_number = response['serialNumber']['value']
    
    # Return the aircraft data
    return response


# Get all engines linked to an aircraft, in this format "{'@context': 'https://schema.lab.fiware.org/ld/context', 'id': 'urn:ngsi-ld:Engine:001', 'type': 'Engine'(...)"
def get_engines_linked_to_aircraft(aircraft_id):
    # Define the Context Broker URL for the aircraft entity
    url_aircraft = f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:{aircraft_id}'
    
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





"""({'id': 'urn:ngsi-ld:Aircraft:001', 'type': 'Aircraft', 'aircraftModel': {'type': 'Property', 'value': 'Boeing 747'}, 
'serialNumber': {'type': 'Property', 'value': 'SN123456'}, 
'manufactureDate': {'type': 'Property', 'value': '2020-01-01T00:00:00Z'}, 
'manufacturedBy': {'type': 'Relationship', 'object': 'urn:ngsi-ld:Manufacturer:001'}, 
'hasEngine': {'type': 'Relationship', 'object': 'urn:ngsi-ld:Engine:001'}})""" 


# Get engine data. Such as id, serial number, manufacturer, maintenance record etc.
def get_engine(engine_id):
    engine = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:{engine_id}')
    engine_response = engine.json()
    
    #engine_id = engine_response['id']
    #serial_number = engine_response['serialNumber']['value']
    
    # Request the engine data
    if engine_response:
        manufacturedBy = engine_response['manufacturedBy']['object']
        hasMaintenanceRecord = engine_response['hasMaintenanceRecord']['object']

        # Request manufacturedBy and hasMaintenanceRecord data
        manufacturedBy_response = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/{manufacturedBy}').json()
        hasMaintenanceRecord_response = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/{hasMaintenanceRecord}').json()

    # Return the engine data
    return engine_response, manufacturedBy_response, hasMaintenanceRecord_response

# Get sensors data from engine in this format "(...)'id': 'urn:ngsi-ld:vibration:001', 'type': 'Vibration', 'isSensorOf': {'type': 'Relationship'(...)"
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

    params = {
    'q': query,
    'orderBy': 'modifiedAt',  # Assuming modifiedAt is the timestamp attribute
    'limit': 1,  # Limit the results to 1 to get the last entry
    'options': 'keyValues'  # Optional: to simplify the output
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

#print("MMMMM")
#print(get_engine('urn:ngsi-ld:Engine:001'))
#print(get_engine_data('001'))
#print(get_all_engines())