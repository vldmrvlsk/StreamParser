import requests
import json

url = 'https://api.twitch.tv/helix/streams'
params = {'user_login': 'имя_канала'}

headers = {'Client-ID': 'ваш_клиент-ид',
           'Authorization': 'Bearer ваш_токен'}

response = requests.get(url, params=params, headers=headers)

data = json.loads(response.text)

if data['data']:
    print('Трансляция началась!')
    print('Название трансляции:', data['data'][0]['title'])
    print('Игра:', data['data'][0]['game_name'])
else:
    print('Трансляция ещё не началась')