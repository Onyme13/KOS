import requests



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



def aircraft(airplane_id):
    aircraft = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Aircraft:{airplane_id}')
    response = aircraft.json()
    aircraft_id = response['id']
    model = response['aircraftModel']['value']
    serial_number = response['serialNumber']['value']
    
    # Return the aircraft data
    return response, aircraft_id, model, serial_number







"""({'id': 'urn:ngsi-ld:Aircraft:001', 'type': 'Aircraft', 'aircraftModel': {'type': 'Property', 'value': 'Boeing 747'}, 
'serialNumber': {'type': 'Property', 'value': 'SN123456'}, 
'manufactureDate': {'type': 'Property', 'value': '2020-01-01T00:00:00Z'}, 
'manufacturedBy': {'type': 'Relationship', 'object': 'urn:ngsi-ld:Manufacturer:001'}, 
'hasEngine': {'type': 'Relationship', 'object': 'urn:ngsi-ld:Engine:001'}}"""



def engine(engine_id):
    engine = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Engine:{engine_id}')
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


def get_engine_data(engine_id):
    """ Retrieve vibration data for a specific engine based on the isSensorOf relationship """
    
    # Define the Context Broker URL
    url = 'http://localhost:1026/ngsi-ld/v1/entities'

    # Define the query parameter with proper syntax
    query = f'isSensorOf=="urn:ngsi-ld:Engine:{engine_id}"'

    # Set the headers
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://schema.lab.fiware.org/ld/context>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
    }

    # Make the GET request
    vibration = requests.get(url, params={'q': query}, headers=headers)
    response = vibration.json()
    vibration_value = response[0]['vibrationValue']['value']
    temperature_value = response[1]['temperatureValue']['value']   
   
   # Return the vibration value and temperature value
    return vibration_value, temperature_value


print(aircraft("001"))
