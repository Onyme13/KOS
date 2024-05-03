import json
import requests


# Entity Creation Example 1 - without context
payload={
  "id": "urn:entities:E13",
  "type": "T",
  "status": {
    "type": "Property",
    "value": "OK"
  },
  "state": {
    "type": "Property",
    "value": "OK"
  }
}
response = requests.post(url='http://localhost:1026/ngsi-ld/v1/entities', headers={
    "content-type": "application/json"},  data=json.dumps(payload))
print(response.status_code)


# Entity Creation Example 2 - with a user context in the payload

payload={
    "@context": {
      "status": "http://a.b.c/attrs/status",
      "state":  "http://a.b.c/attrs/state"
    },
    "id": "urn:entities:E2",
    "type": "T",
    "status": {
      "type": "Property",
      "value": "From Core Context"
    },
    "state": {
      "type": "Property",
      "value": "From User Context"
    },
    "state2": {
      "type": "Property",
      "value": "From Default URL"
    }
}

response = requests.post(url='http://localhost:1026/ngsi-ld/v1/entities', headers={
    "content-type": "application/json"},  data=json.dumps(payload))
print(response.status_code)