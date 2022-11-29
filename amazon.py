import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
HEADERS = { 'Accept-Language' : 'en-US', 'User-Agent': user_agent}

def list_printer(name: list):
    for i in range(0, len(name)):
        print(name[i].text)

url = 'https://www.amazon.com/s?k=macbook+air'
r = requests.get(url, headers=HEADERS)
print(r)



