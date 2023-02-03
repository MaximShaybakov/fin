from datetime import datetime as dt
import requests

base_url = 'http://127.0.0.1:8000/api/v1/'
update = 'partner/update/'
register = 'user/register/'
login = 'user/login/'
detail = 'user/details/'
TOKEN_vasja = 'Token 33667d0bc49e1fea2d4396e0ee0e4934bcc93bb1'
headers = {"email": "vasya-pupkin@mail.com", "password": "vasya-pupkin123"}
new_user = {'first_name': 'jorik',
            'last_name': 'vartanov',
            'email': 'jorvar@mail.ru',
            'password': 'jkhgci787ghj',
            'company': 'yandex',
            'position': 'engineer',
            'type': 'shop'}
new_shop = {'first_name': 'jorik',
            'last_name': 'vartanov',
            'email': 'jorvar@mail.ru',
            'password': 'jkhgci787ghj',
            'company': 'yandex',
            'type': 'shop'}

data = requests.get(base_url + detail,
                    data={'Content-type': 'application/json',
                          'Authorization': f'{TOKEN_vasja}',
                          "email": "vasya-pupkin@mail.com",
                          "password": "vasya-pupkin123"
                          },
                    timeout=2)

# data = requests.post(base_url + login, json={"email": "vasya-pupkin@mail.com",
#                                              "password": "vasya-pupkin123"},)

# data = requests.post(base_url + register, data=new_shop, timeout=3)
# data = requests.post(base_url + detail, json={'Authenticated': 'Token 33667d0bc49e1fea2d4396e0ee0e4934bcc93bb1'})
print(data.url, data.status_code, data.request)
print(data.json())
