import requests
import base64
wp_user ='aouwal'
wp_pass ='fBRb DJSn FU06 SMfY 2NPJ Gq6v'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

data = {'title':'This is awesome title'}
wp_post_url = 'https://localhost/wp/wp-json/wp/v2/posts'
res = requests.post(wp_post_url, data=data, headers=wp_headers, verify=False)
print(res.status_code)
print(res.json())


