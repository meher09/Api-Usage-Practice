import requests
api_key = 'AIzaSyCACkMStcfbxpo7q4Y-cPAVS2q8RvqIKIU'
test_url = input("Enter url: ")
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'

res = requests.get(api_url)
if res.status_code == 200:
   data = res.json()
   cls_score = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
   print(cls_score)
else:
    print('Something wrong')