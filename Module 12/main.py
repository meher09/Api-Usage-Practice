from requests import get
API_KEY = '31948480-5d5a51ffa225e1fccf84b00ff'
query = 'yellow+flowers'
api_url = f'https://pixabay.com/api/?key={API_KEY}&q={query}'

r = get(api_url)
api_data = r.json().get('hits')

for data in api_data:
    image_url = data.get('webformatURL')
    file = open('images.txt','a+')
    file.writelines(image_url+'\n')
    file.close()