import requests
import base64

user= 'aouwal'
password = '2ARi HWAI eWV7 Z2s1 1WZc Ix2t'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}






media_upload('dog food.png')

