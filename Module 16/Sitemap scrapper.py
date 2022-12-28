import requests
from bs4 import BeautifulSoup as bs
url = 'https://www.discovermagazine.com/sitemap/article/technology/1.xml'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
locs = soup.findAll('loc')
for loc in locs:
    print(loc.text)