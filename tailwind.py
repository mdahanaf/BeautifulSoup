import requests
from bs4 import BeautifulSoup

def item_tester(col1: list, col2: list, col3: list):

    for i in range(0, len(col1)):
        vv = col1[i].text
        vv.replace(',', '.')
        print(col1[i].text,',',col2[i].text,',',col3[i].text)


url = 'https://jobs.tailwindcss.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

company = soup.find_all('dd', class_='text-xs font-semibold leading-6 text-gray-900')
title = soup.find_all('dd', class_='text-[0.9375rem] font-semibold leading-6 text-gray-900')
type = soup.find_all('dd', class_='text-xs leading-6 text-gray-600')

# print(title[0])
print('company, title, type')
item_tester(company, title, type)


