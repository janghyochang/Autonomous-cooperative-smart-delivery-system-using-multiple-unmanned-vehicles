import requests

url = "http://203.253.128.161:7579/Mobius/cssrj/Drone/rsp_drone/coordinate/la"

payload = {}
headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
}

response = requests.request("GET", url, headers=headers, data=payload)

new_json = response.json()
res = new_json["min:cin"]['con']
print(res)
