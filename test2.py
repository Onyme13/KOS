from queries import *
import re



print(get_engine_data('urn:ngsi-ld:Engine:001'))
data = get_engine_data('urn:ngsi-ld:Engine:001')

pattern = r"urn:ngsi-ld:(.*)"
engine_data = []

engine_data.append({
                    #"engine": re.sub(pattern,r"\1" ,engine['id']),
                    "vibration": data[-2]['vibrationValue']['value'],
                    "temperature": data[-1]['temperatureValue']['value']
                })


print(engine_data)
