import requests
from pprint import pprint
from wpFunc import image_url,list_html_list, dict_list, headers, wph2,openai_text


api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
r = requests.get(api_url)
meals = r.json().get('meals')

single_meal = meals[0]
meal_area = single_meal.get('strArea')
meal_name = single_meal.get('strMeal')
instruction = single_meal.get('strInstructions')
image = single_meal.get('strMealThumb')
youtube = single_meal.get('strYoutube')

i = 1

ingredients = {}

while i < 21:
    key_ingredient = f'strIngredient{i}'
    key_measurment = f'strMeasure{i}'
    if (single_meal.get(key_ingredient) != None) and (single_meal.get(key_ingredient) != ''):
       ingredients[single_meal.get(key_ingredient)] = single_meal.get(key_measurment)

    i = i+1

instruction_list = instruction.split('\r\n')

title = f'{meal_name} Recepie'
intro = openai_text(f'write about {meal_area} {meal_name}')
image = image_url(image,title)

heading_first = wph2('Ingredients')
ingredients_html = dict_list(ingredients)
heading_second = wph2('Description')
description =list_html_list(instruction_list)
content = f'{intro}{image}{heading_first}{ingredients_html}{heading_second}{description}'

data = {
    'title':title,
    'content':content
}

headers = headers('aouwal', '7wWI nn4N nLyx XEF3 HeLT Q2xN')
endpoint =  'https://mysite.local/wp-json/wp/v2/posts'
r = requests.post(endpoint, data=data,headers=headers, verify=False)
print(r)

