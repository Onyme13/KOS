import json
import random
from datetime import datetime, timedelta
import time

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

def generate_sensor_data(sensor_type, engine_id, date, unit, range_min, range_max):
    return {
        "id": f"urn:ngsi-ld:{sensor_type.lower()}:{engine_id.split(':')[-1]}",
        "type": sensor_type,
        f"{sensor_type.lower()}Value": {"type": "Property", "value": random.uniform(range_min, range_max)},
        f"{sensor_type.lower()}Unit": {"type": "Property", "value": unit},
        f"{sensor_type.lower()}Time": {"type": "Property", "value": date},
        "isSensorOf": {"type": "Relationship", "object": engine_id}
    }

def generate_aircraft_data():
    models = ["Boeing 747", "Airbus A320", "Boeing 777", "Airbus A380"]
    engines = ["Model X", "Model Y", "Model Z"]
    manufacturers = ["Boeing", "Airbus", "Lockheed Martin"]
    manufacturer_ids = ["001", "002", "003"]
    maintenance_details = ["Engine oil change", "Tire replacement", "Brake inspection"]

    data = []
    
    # Generate aircrafts
    for i in range(1, 6):
        aircraft_id = f"urn:ngsi-ld:Aircraft:{i:03}"
        engine_id = f"urn:ngsi-ld:Engine:{i:03}"
        manufacturer_index = random.randint(0, len(manufacturers) - 1)
        manufacturer_id = f"urn:ngsi-ld:Manufacturer:{manufacturer_ids[manufacturer_index]}"
        sensor_date = random_date(datetime(2020, 1, 1), datetime(2021, 1, 1)).isoformat()

        aircraft = {
            "id": aircraft_id,
            "type": "Aircraft",
            "aircraftModel": {"type": "Property", "value": random.choice(models)},
            "serialNumber": {"type": "Property", "value": f"SN{random.randint(100000, 999999)}"},
            "manufactureDate": {"type": "Property", "value": random_date(datetime(2010, 1, 1), datetime(2020, 1, 1)).isoformat()},
            "manufacturedBy": {"type": "Relationship", "object": manufacturer_id},
            "hasEngine": {"type": "Relationship", "object": engine_id}
        }
        data.append(aircraft)

        engine = {
            "id": engine_id,
            "type": "Engine",
            "engineModel": {"type": "Property", "value": random.choice(engines)},
            "serialNumber": {"type": "Property", "value": f"SN{random.randint(100000, 999999)}"},
            "manufactureDate": {"type": "Property", "value": random_date(datetime(2010, 1, 1), datetime(2020, 1, 1)).isoformat()},
            "manufacturedBy": {"type": "Relationship", "object": manufacturer_id},
            "hasMaintenanceRecord": {"type": "Relationship", "object": f"urn:ngsi-ld:Maintenance:{i:03}"}
        }
        data.append(engine)

        vibration = generate_sensor_data("Vibration", engine_id, sensor_date, "m/s2", 0.0, 1.0)
        temperature = generate_sensor_data("Temperature", engine_id, sensor_date, "Celsius", -10, 120)

        data.extend([vibration, temperature])

        maintenance = {
            "id": f"urn:ngsi-ld:Maintenance:{i:03}",
            "type": "Maintenance",
            "lastMaintenanceDate": {"type": "Property", "value": random_date(datetime(2020, 1, 2), datetime(2021, 1, 1)).isoformat()},
            "nextMaintenanceDate": {"type": "Property", "value": random_date(datetime(2021, 1, 2), datetime(2022, 1, 1)).isoformat()},
            "maintanceDetails": {"type": "Property", "value": random.choice(maintenance_details)}
        }
        data.append(maintenance)

    # Generate manufacturers
    for index, name in enumerate(manufacturers):
        manufacturer = {
            "id": f"urn:ngsi-ld:Manufacturer:{manufacturer_ids[index]}",
            "type": "Manufacturer",
            "manufacturerName": {"type": "Property", "value": name},
            "manufacturerAddress": {"type": "Property", "value": "Seattle, USA"},
            "manufacturerContact": {"type": "Property", "value": "example@email.com"}
        }
        data.append(manufacturer)

    return data

# Generate and print the data

while True:
        
    aircraft_data = generate_aircraft_data()
    print(json.dumps(aircraft_data, indent=4))
    time.sleep(5)
