from pyfiglet import figlet_format
from termcolor import colored

msg= input("What would you like to print? ")
color= input("What color? ")

ascii_art=figlet_format(msg)

try:
	colored_ascii=colored(ascii_art,color=color)
except KeyError:
	print("Color must be one of - red, green, yellow, blue, magenta, cyan or white ")
	print("Using default of white")
	colored_ascii=colored(ascii_art,color="white")

print(colored_ascii)
