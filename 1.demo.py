# step 1 : Intsall All Requirement

import requests
from bs4 import BeautifulSoup

url = "http://localhost/webscraping/demo.html"



# step 2 : Get HTML Content (which is in 'bytes' type)

r = requests.get(url)     # r is 'requests.model.Respons' object

html_content = r.content

# print(html_content)




# step 3 : Parse HTML Content

soup = BeautifulSoup(html_content,"html.parser") # soup is beautifulsoup's Object

# print(soup)			#soup.prittify print html content in well format




# setp 4 : Traverse HTML Content

title = soup.find('title')								# Comman Type Of Objects
														# 1) Tag Object (title)
# print(type(title))									# 2) Navigable String Object (title.string)
# print(type(title.string))								# 3) Beautifulsoup Object (soup)
														# 4) Comment Object ()
print(title.get_text())
print("---------------------------------")


# Comment Object

# com = "<p><!--Hello--></p>"
# soup2 = BeautifulSoup(com)
# print(type(soup2.p.string))


# how to find all paragrphs

para = soup.find_all('p')
# print(para)

# how to find all <a> tags (anchor tags)

# anchor = soup.find_all('a')				#find any tag using find_all() function
# print(anchor)

# Find First Paragraph tag

# print(soup.find('p'))

# Find Class of First Paragraph

# print(soup.find('p')['class'])
# print(soup.find('p').get('class'))

# Find id of First Paragraph

# print(soup.find('p')['id'])

# Find Perticular paragraph using class

# print(soup.find_all('p',class_='para1'))

# Find Paragraph String

# print(soup.find('p').get_text())
# print(soup.find('p',class_='para1').get_text())
# print(soup.get_text())


# Find Links in <a> tag

# anchor_all = soup.find_all('a')

# links = set()

# for anchor_tag in anchor_all:
# 	if anchor_tag.get('href') != '#':
# 		links.add(anchor_tag.get('href'))

# print(links)

# .contents : A children's tags are available as a list    (store in memory)
# .children : A children's tags are available as a generator(iterator) (not store in memory)

tag = soup.find(id='one')

#print all element in tag

# for elements in tag.contents:
# 	print(elements)

# print all strings in tag 

# for strings in tag.strings:
# 	print(strings)

# print all strings(stripped) in tag

# for strings in tag.stripped_strings:
# 	print(strings)


# siblings

# print("\n--------------------")

# print(tag.next_sibling)			# Print next sibling(blank line also a sibling)
# print('------')
# print(tag.next_sibling.next_sibling) # Print next to next sibling
# print('------')
# print(tag.previous_sibling)
# print('------')
# print(tag.previous_sibling.previous_sibling)

css = soup.select('#one')
print(css)