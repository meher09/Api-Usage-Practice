import openai
import base64
import requests

openai.api_key = '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'


def wph2(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code


def wpp(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code


def oai_answer(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output


keyword = input("enter your keyword: ")
prompt = f'write three questions about {keyword}'
content = wpp(oai_answer(f'write short intro about {keyword}').strip().strip('\n'))
questions = oai_answer(prompt)
questions_list = questions.strip().split('\n')
end_line = 'write a paragraph about it'

qna = {}
for q in questions_list:
    command = f'{q} {end_line}'
    answer = oai_answer(command).strip().strip('\n')
    qna[q] = answer

user = 'aouwal'
password = '2ARi HWAI eWV7 Z2s1 1WZc Ix2t'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}


def wpi(id, src, keyword):
    line_one = f'<!-- wp:image {{"align":"center","id":{id},"sizeSlug":"full","linkDestination":"none"}} -->'
    line_two = f'<figure class="wp-block-image aligncenter size-full"><img src="{src}" alt="{keyword}" class="wp-image-{id}" />'
    line_three = f'<figcaption class="wp-element-caption">{keyword}</figcaption></figure><!-- /wp:image -->'
    code = f'{line_one}{line_two}{line_three}'
    return code


def media_upload(image):
    media_url = 'https://mysite.local/wp-json/wp/v2/media'
    files = {'file': open(image, 'rb')}
    res = requests.post(media_url, files=files, headers=headers, verify=False)
    data = res.json()
    id = data.get('id')
    src = data.get('guid').get('rendered')
    image_code = wpi(id, src, keyword)
    return image_code


content += media_upload('dog food.png')

for key, value in qna.items():
    qn = wph2(key)
    ans = wpp(value)
    temp = qn + ans
    content += temp

title = f'common questions about {keyword}'

data = {
    'title': title.title(),
    'content': content,
    'slug': keyword.replace(' ', '-'),
    'featured_media': '10'
}
api_url = 'https://mysite.local/wp-json/wp/v2/posts'
r = requests.post(api_url, data=data, headers=headers, verify=False)
