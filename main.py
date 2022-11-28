import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

def get_url(position, location):
    template = 'https://in.indeed.com/jobs?q={}&l={}'
    url2 = template.format(position, location)

    return url2
    

# job_title = input("What's the job title? ")
# job_title = job_title.replace(" ", "+")

# url = get_url('web developer', 'mumbai')
url = 'https://jobs.tailwindcss.com/'
python_jobs = 'https://www.python.org/jobs/?page=1'
indeed = 'https://in.indeed.com/jobs?q=web+developer&l=delhi'
# url = 'https://www.amazon.com/s?k=macbook+pro&crid=2FOTI3C5FA8ZS&sprefix=mac%2Caps%2C379&ref=nb_sb_ss_ts-doa-p_1_3'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
HEADERS = { 'Accept-Language' : 'en-US', 'User-Agent': user_agent}

response = requests.get(indeed, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

# company = soup.find_all('dd', 'text-xs font-semibold leading-6 text-gray-900')
# title = soup.find_all('dd', class_='text-[0.9375rem] font-semibold leading-6 text-gray-900')

# for i in range(0, len(title)):
#     c = company[i].text
#     t = title[i].text
#     print(c, " - ", t)

name = soup.find_all('td', class_='resultContent')

print(response)
print(name)

