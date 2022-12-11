from httpx import get
from pprint import  pprint
base_url = 'https://www.cocooncityhostel.com/wp-json/wp/v2'

page_api = f'{base_url}/pages?page=2'
r = get(page_api)
api_data = r.json()

for page in api_data:
    try:
        print(page.get('link'))
    except:
        print('Page Not Found')
