import requests
import csv
from bs4 import BeautifulSoup

file = open("sp.csv","w")
writer = csv.writer(file,delimiter=',',quotechar='"')

url = 'http://localhost/smartphones/smartphone.html'
r = requests.get(url)

html_content = r.content

soup = BeautifulSoup(html_content,'html.parser')

tags = soup.find_all('th')

heads = []

for onetag in tags:
	heads.append(onetag.get_text().strip())

writer.writerow(heads)

tds = soup.find_all('td')
td = []
for onetd in tds:
	td.append(onetd.get_text().strip())

n=len(tds)
for i in range(1,n+1,3):
	writer.writerow([td[i-1],td[i],td[i+1]])
print("header added successfully")