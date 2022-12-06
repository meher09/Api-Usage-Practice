import requests
res = requests.get('https://jsonplaceholder.typicode.com/posts')
print(res.json())
