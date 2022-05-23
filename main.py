import requests
from bs4 import BeautifulSoup

URL = 'https://home.1k.by/kitchen-coffeemakers/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
res = soup.find_all('a', class_='prod__link')
cof = []


with open('coffee.txt','w',encoding='utf-8') as file:
    for r in res:
        file.write(f'{r.text.strip()}\n')