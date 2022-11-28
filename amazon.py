import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
HEADERS = { 'Accept-Language' : 'en-US', 'User-Agent': user_agent}

def list_printer(name: list):
    for i in range(0, len(name)):
        print(name[i].text)


def result():
    
    ll: list = []
    
    for i in range(1, len()+1):
        url = f'https://www.ultratech.com.bd/ram?page={i}'
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find_all('div', 'name')
        ll.append(title[i].text)










list_printer(title)