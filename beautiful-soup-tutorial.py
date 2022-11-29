# importing all necessary module
import requests
from bs4 import BeautifulSoup

# targeted url
url = 'https://www.codewithharry.com/'

# sending the response request
r = requests.get(url)

# getting html content
htmlContent = r.content

# creating html Tree structure(soup), using html.parser
soup = BeautifulSoup(htmlContent, "html.parser")

# printing the title of the targeted webpage
title = soup.title
# print(title.text)

# printing all paragraph(p) tags of that webpage
paras = soup.find_all('p')
# print(paras)

# printing all anchor(a) tags of that webpage
anchor = soup.find_all('a')
# print(anchor)

# get first paragraph(p) tag
pp = soup.find('p')
# print(pp)

#getting the class of any tag
classes = soup.find('p')['class']
# print(classes)
# type of 'classes' variable
# print(type(classes))

# getting the value of 'href' attribute from first anchor(a) tag
href = soup.find('a')['href']
# print(href)

#find all tags that contains 'flex' value in the class attribute
flex = soup.find_all(class_='flex')
# print(flex)

# get the text from the element with particular class
text_sm = soup.find('button', class_='text-sm')
# print(text_sm.text)

#get all links from anchro tag
ll = soup.find_all('a')
for x in ll:
    ii = "https://www.codewithharry.com"
    # print(ii+x.get('href'))

print(soup.p)

