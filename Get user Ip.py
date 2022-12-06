import requests
api_url = 'https://api.ipify.org?format=json'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    ip = data.get('ip')
    print('Your Ip Address is',ip)
