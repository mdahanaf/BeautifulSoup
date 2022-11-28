import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

HEADERS = { 'Accept-Language' : 'en-US', 'User-Agent': user_agent}

url = 'https://www.amazon.jobs/en/search?base_query=Software+Engineer&loc_query=Remote&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county='
url2 = 'https://careers.google.com/jobs/results/?distance=50&hl=en_US&jlo=en_US&q=Software%20Engineer'
response = requests.get(url2, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

print(response)
print(soup.find_all('h2', class_='gc-card__title gc-heading gc-heading--beta'))
