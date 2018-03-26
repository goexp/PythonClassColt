import requests
import yaml

cfg_files=["google_api_keys.yml","my_info.yml"]
cfg={}

for cfg_file in cfg_files:
	with open(cfg_file,"r") as ymlfile:
		cfg[cfg_file]= yaml.load(ymlfile)

url="https://maps.googleapis.com/maps/api/geocode/json"

response= requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"address":cfg["my_info.yml"]["address"], "key":cfg["google_api_keys.yml"]["map_api_key"]}
	)

data=response.json()

print(data["results"][0].keys())
print(data["results"][0].get("formatted_address"))
print(data["results"][0].get("geometry").get("location"))