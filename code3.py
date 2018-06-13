from bs4 import BeautifulSoup
import requests
url=raw_input("Enter website: ")
r=requests.get("http://"+url)
data=r.text
soup=BeautifulSoup(data)
for link in soup.find_all('a'):
	print link.get('href')
