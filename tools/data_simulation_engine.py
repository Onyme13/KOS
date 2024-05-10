import json
import random
from datetime import datetime, timedelta
import time

# Initialize some base data with IDs, types, and relationships
vibration_template = {
    "id": "urn:ngsi-ld:vibration:001",
    "type": "Vibration",
    "vibrationValue": {"type": "Property", "value": 0.5},
    "vibrationUnit": {"type": "Property", "value": "m/s2"},
    "vibrationTime": {"type": "Property", "value": "2020-01-01T00:00:00Z"},
    "isSensorOf": {"type": "Relationship", "object": "urn:ngsi-ld:Engine:001"}
}

temperature_template = {
    "id": "urn:ngsi-ld:temperature:001",
    "type": "Temperature",
    "temperatureValue": {"type": "Property", "value": 50},
    "temperatureUnit": {"type": "Property", "value": "Celsius"},
    "temperatureTime": {"type": "Property", "value": "2020-01-01T00:00:00Z"},
    "isSensorOf": {"type": "Relationship", "object": "urn:ngsi-ld:Engine:001"}
}

# Function to generate a new timestamp based on the current time
def get_current_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# Simulate sensor data every second
while True:
    # Randomize the values slightly for simulation purposes
    vibration_value = round(random.uniform(0.1, 2.0), 2)
    temperature_value = round(random.uniform(20, 80), 1)

    # Update the templates with new values and timestamps
    vibration_data = vibration_template.copy()
    temperature_data = temperature_template.copy()

    vibration_data['vibrationValue']['value'] = vibration_value
    vibration_data['vibrationTime']['value'] = get_current_timestamp()

    temperature_data['temperatureValue']['value'] = temperature_value
    temperature_data['temperatureTime']['value'] = get_current_timestamp()

    # Print as JSON (or handle as required)
    print(json.dumps(vibration_data, indent=4))
    print(json.dumps(temperature_data, indent=4))

    # Wait for 1 second before generating the next batch
    time.sleep(1)
