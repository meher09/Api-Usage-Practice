import requests
import base64
from pprint import pprint

user = 'aouwal'
password = 'KL9x RbJa i4Il bN4y PL0S KuBw'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headers = {'Authorization':f'Basic {token.decode("utf-8")}'}

def wp_paragraph(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code


title = 'What is Lorem Ipsum?'
paragraph = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

content = wp_paragraph(paragraph)
content_data = {
    'title': title,
    'content': content,
    'categories': '102'
}
api_end_point = 'https://localhost/wp/wp-json/wp/v2/posts'
r = requests.post(api_end_point, data=content_data, headers=headers, verify=False)
print(r.status_code)
