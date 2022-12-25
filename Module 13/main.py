import base64
import requests
from phoneFunc import slugify, wp_image,wp_table


data_url = 'https://mobile-phone-server.vercel.app/phones'
res = requests.get(data_url)
data = res.json()
phone_data = data.get('RECORDS')
phone = phone_data[0]
# Data get
name = phone.get('name')
image = phone.get('picture')
brand = name.split()[0]
released = phone.get('released_at')
body = phone.get('body')
os = phone.get('os')
storage = phone.get('storage')
display = phone.get('display_size')
resolution = phone.get('display_resolution')
camera = phone.get('camera_pixels')
video = phone.get('video_pixels')
ram = phone.get('ram')
chipset = phone.get('chipset')
battery_type = phone.get('battery_type')
battery_size = phone.get('battery_size')
specification = phone.get('specifications')

# Data Processing
title = f'{name} price in Bangladesh'
slug = slugify(name)
image_alt = f'{name} image'
image_cap = f'{name} Picture'
dict_one = {'Name': name, 'Brand': brand, 'Launched': released}



# Wordpress configutation
user = 'aouwal'
password = 'Tcqv imOJ 3Ykx z4cr OFC2 i1ar'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headers = {'Authorization':f'Basic {token.decode("utf-8")}'}
post_api = 'https://localhost/wp/wp-json/wp/v2/posts'


# Wordpress Data
image_code = wp_image(image, image_alt, image_cap)
table_one = wp_table(dict_one)
content = f'{image_code}{table_one}'

#Wordpress Data
data = {
    'title': title,
    'slug': slug,
    'content': content
}

res = requests.post(post_api, data = data, headers=headers, verify=False)
print(res.json())




