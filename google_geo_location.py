import requests
import yaml

with open("google_api_keys.yml","r") as ymlfile:
	cfg= yaml.load(ymlfile)

api_key=cfg["map_api_key"]

with open("my_info.yml","r") as ymlfile:
	cfg= yaml.load(ymlfile)

address=cfg["address"]

url="https://maps.googleapis.com/maps/api/geocode/json"

response= requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"address": address,"key":api_key}
	)

data=response.json()

print(data["results"][0].keys())
print(data["results"][0].get("formatted_address"))
print(data["results"][0].get("geometry").get("location"))