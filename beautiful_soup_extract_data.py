
from bs4 import BeautifulSoup
with open("sample.html") as file_handle:
	html=file_handle.read()

soup= BeautifulSoup(html,"html.parser")
print("---The complete document---")
print(soup)
print("---The body---")
print(soup.body)
print("---id=first css sytle selector . data ---") 
print(soup.select(".special")[0].get_text())
print("---id=first css sytle selector . data ---") 
for obj in soup.select(".special"):
	print(obj.name)
	print(obj.attrs)
print("---find via header and select [data-example] ---") 
print(soup.find("h3")["data-example"])
print("---find via div and select [id] ---") 
print(soup.find("div")["id"])




