import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice as rnd_choice

url = "https://icanhazdadjoke.com/search"

print(colored(figlet_format("Dad Joke 3000"),color="white"))

joke_topic=input("Let me tell you a joke! Give me a topic: ")

response= requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term": joke_topic}
	)

data=response.json()

jokes=data["results"]
if len(jokes) == 0:
	print(f"Sorry, I have no jokes about {joke_topic}.")
elif len(jokes) == 1:
	print(f"I've got one joke about {joke_topic}. Here it is:")
	print(rnd_choice(jokes).get("joke",""))
else:
	print(f"I've got {len(jokes)} jokes about {joke_topic}. Here's one:")
	print(rnd_choice(jokes).get("joke",""))
#print(data["joke"])
#print(f"status: {data['status']}")