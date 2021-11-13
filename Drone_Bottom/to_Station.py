import requests

url = "http://203.253.128.161:7579/Mobius/cssrj/Drone_station/to_Station"

payload = "{\n    \"m2m:cin\": {\n        \"con\": \"Open_Station\"\n    }\n}"
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': '{{aei}}',
  'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
}

response = requests.request("POST", url, headers=headers, data=payload)
