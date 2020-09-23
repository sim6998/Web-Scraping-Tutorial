import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/selenium-python-tutorial/'

r = requests.get(url)
html_content = r.content

soup = BeautifulSoup(html_content,"html.parser")

div = soup.find_all('a')

for anchor in div:
	if anchor.get_text() == "Selenium Basics" :
		print(anchor.get_text(),':')
		print(anchor.get('href'))

	if anchor.get_text() == "Components of Selenium":
		print(anchor.get_text(),':')
		print(anchor.get('href'))