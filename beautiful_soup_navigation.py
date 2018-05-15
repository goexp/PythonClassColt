
from bs4 import BeautifulSoup
with open("sample.html") as file_handle:
	html=file_handle.read()

#.contents goes forward .parent goes backward

soup= BeautifulSoup(html,"html.parser")
print("---The complete document---")
print(soup)
print("---The contents of the body---")
print(soup.body.contents)
print("---The first element of the body, because of newline---")
print(soup.body.contents[1])
print("---The first element of the body, because of newline and contents---")
print(soup.body.contents[1].contents)
print("---The first element of the body, because of newline / next sibling---")
print(soup.body.contents[1].next_sibling)
print("---The first element of the body, because of newline / next sibling .next_sibling---")
print(soup.body.contents[1].next_sibling.next_sibling)
print("---find class special parent---")
print(soup.select(".special")[0].parent)
print("---find class special parent and go one more up---")
print(soup.select(".special")[0].parent.parent)
print("---find id first and next sibling---")
print(soup.find(id="first").find_next_sibling()) #better
print("---find id first and next sibling and next---")
print(soup.find(id="first").find_next_sibling().find_next_sibling()) 
print("---select attribute previous sibbling---")
print(soup.select("[data-example]")[1].find_previous_sibling())
print("---find h3 and find parent---")
print(soup.find("h3").find_parent())

