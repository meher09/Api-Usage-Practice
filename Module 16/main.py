from bs4 import BeautifulSoup
import requests
url = "https://quotes.toscrape.com/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')
heading = soup.find('h1')
print(heading.text)

link = soup.find('a')
print(link.text)