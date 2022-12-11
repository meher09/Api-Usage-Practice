from requests import get
from pprint import pprint
API_KEY = '1187ffc7690886f66d0589689f2a01f0'
city_name = 'Dhaka'
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

r = get(api_url)

api_data = r.json()
country_name = api_data.get('sys').get('country')
weather_data = api_data.get('main')
feels_like = weather_data.get('feels_like')
temp = weather_data.get('temp')
maximum_temp = weather_data.get('temp_max')

print(country_name, temp, maximum_temp, feels_like)