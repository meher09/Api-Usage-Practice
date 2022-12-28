import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title.text)
links = soup.findAll('a')
for link in links:
    print('https://quotes.toscrape.com'+link.get('href'))