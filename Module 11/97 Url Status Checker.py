import httpx
url_list = [
    'https://www.dogfoodadvisor.com/best-dog-foods/best-dry-dog-foods/',
    'https://money.com/best-dog-food/',
    'https://www.nbcnews.com/select/shopping/best-dog-food-ncna1189551'
]

for url in url_list:
    r = httpx.get(url)
    print(url,r.status_code, sep="--------")
