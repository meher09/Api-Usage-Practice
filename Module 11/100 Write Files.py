import httpx
url_list = [
    'https://www.dogfoodadvisor.com/best-dog-foods/best-dry-dog-foods/',
    'https://money.com/best-dog-food/',
    'https://www.nbcnews.com/select/shopping/best-dog-food-ncna1189551'
]

for url in url_list:
    r = httpx.get(url)
    text = f'{url}--------{r.status_code}'
    file = open('link status.txt', 'a+')
    file.writelines(text+'\n')
    file.close()


file = open('link status.txt', 'r+')
urllist = file.readlines()
file.close()

print(urllist)


# text = 'This is simple Text 3'
# file = open('abcd.txt','a+')
# file.writelines(text+'\n')
# file.close()