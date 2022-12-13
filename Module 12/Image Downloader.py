from requests import get
file = open('images.txt', 'r+')
url_list=file.readlines()
file.close()

new_url_list = []
for url in url_list:
    new_url = url.rstrip('\n')
    new_url_list.append(new_url)



single_url = new_url_list[0]
r = get(single_url)
with open('Google.jpg', 'wb') as file:
    file.write(r.content)



