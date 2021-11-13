import requests

url = "http://203.253.128.161:7579/Mobius/cssrj/turtlebot/la"
payload = {}
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'
}

response = requests.request("GET", url, headers=headers, data = payload)


new_json = response.json()
#print(type(new_json))
#print(new_json["m2m:cin"]['con'])
res=new_json["m2m:cin"]['con']
