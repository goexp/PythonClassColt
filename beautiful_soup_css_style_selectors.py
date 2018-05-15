
from bs4 import BeautifulSoup
with open("sample.html") as file_handle:
	html=file_handle.read()

soup= BeautifulSoup(html,"html.parser")
print("---The complete document---")
print(soup)
print("---The body---")
print(soup.body)
print("---id=first css sytle selector #---") 
print(soup.select("#first"))
print("---id=first css sytle selector .---") 
print(soup.select(".special"))
print("---id=first css sytle selector div---") 
print(soup.select("div"))
print("---id=first css sytle selector attribute []---") 
print(soup.select("[data-example]"))

