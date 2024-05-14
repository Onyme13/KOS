import requests


def aircraft(airplane_id):
    aircraft = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Aircraft:{airplane_id}')
    response = aircraft.json()
    aircraft_id = response['id']
    model = response['aircraftModel']['value']
    serial_number = response['serialNumber']['value']
    


def engine(engine_id):
    engine = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Engine:{engine_id}')
    engine_response = engine.json()
    
    #engine_id = engine_response['id']
    #serial_number = engine_response['serialNumber']['value']
    
    # Request the engine data
    if engine_response:
        manufacturedBy = engine_response['manufacturedBy']['object']
        hasMaintenanceRecord = engine_response['hasMaintenanceRecord']['object']

        # Request 

        manufacturedBy = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/{manufacturedBy}')
        manufacturedBy_response = manufacturedBy.json()

        hasMaintenanceRecord = requests.get(url=f'http://localhost:1026/ngsi-ld/v1/entities/{hasMaintenanceRecord}')
        hasMaintenanceRecord_response = hasMaintenanceRecord.json()

    print(engine_response,manufacturedBy_response,hasMaintenanceRecord_response)


def get_engine_data(engine_id):
    """        "isSensorOf": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:Engine:001"
        }"""
    pass
        


engine("001")
aircraft("001")