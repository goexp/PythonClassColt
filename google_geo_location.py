import requests
import yaml

with open("google_api_keys.yml","r") as ymlfile:
	cfg= yaml.load(ymlfile)

api_key=cfg["map_api_key"]
url="https://maps.googleapis.com/maps/api/geocode/json"

response= requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"address": "2300 winners cir, springfield, il","key":api_key}
	)

data=response.json()

print(data)