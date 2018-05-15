
from bs4 import BeautifulSoup
with open("sample.html") as file_handle:
	html=file_handle.read()

soup= BeautifulSoup(html,"html.parser")
print("---The complete document---")
print(soup)
print("---The body---")
print(soup.body)
print("---div tag using .div---") #Prints only the first dive tag
print(soup.body.div)
print("---div tag using .find('div')---") #Prints only the first div tag
print(soup.body.find("div"))
print("---div tag using .find_all('div')---") #Prints all the div tags
print(soup.find_all("div"))
print("---div tag using .find_all('li')---") #Prints all the div tags
print(soup.find_all("li"))
print("---id using .find(id='first')---") #Prints all the div tags
print(soup.find(id="first"))
print("---class using .find_all(class_='special')---") #Prints all the div tags
print(soup.find_all(class_="special"))
print("---attrs using .find_all(class_='special')---") #Prints all the div tags
print(soup.find_all(attrs={"data-example":"yes"}))
