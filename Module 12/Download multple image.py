from requests import get
with open('images.txt', 'r') as file:
    url_list = file.readlines()

i= 0
for url in url_list:
    url = url.strip('\n')
    r = get(url)
    with open(f'images/{i}.jpg', 'wb') as file:
        file.write(r.content)
    # i = i+1
    i += 1

