import requests
from pprint import pprint

base_url = 'http://127.0.0.1:8000/api/v1/'
update = 'partner/update/'
register = 'user/register/'
login = 'user/login/'
detail = 'user/details/'
category = 'categories/'
products = 'products/'
TOKEN_vasja = 'Token 33667d0bc49e1fea2d4396e0ee0e4934bcc93bb1'
TOKEN_vagran = 'Token f05313c2a9fcbf64ba2392b94110d95f3122257c'
headers = {"email": "vasya-pupkin@mail.com", "password": "vasya-pupkin123"}
new_user = {'first_name': 'vagran',
            'last_name': 'vartanov',
            'email': 'vagvar@mail.ru',
            'password': 'sgers64$',
            'company': 'yandex',
            'position': 'engineer'}
new_shop = {'first_name': 'jorik',
            'last_name': 'vartanov',
            'email': 'jorvar@mail.ru',
            'password': 'jkhgci787ghj',
            'company': 'yandex',
            'type': 'shop'}

'''User detail info '''
# data = requests.get(base_url + detail,
#                     headers={'Content-type': 'application/json',  # headers!!!
#                           'Authorization': f'{TOKEN_vagran}',
#                           "email": "vagvar@mail.ru",
#                           "password": "sgers64$"},
#                     timeout=2)

'''User login'''
# data = requests.post(base_url + login, headers={'Content-type': 'application/json',  # headers!!!
#                                              'Authorization': f'{TOKEN_vagran}',
#                                              'email': 'vagvar@mail.ru',
#                                              'password': 'sgers64$'})

'''Register new user'''
# data = requests.post(base_url + register, data=new_user, timeout=3)  # data!!!

'''Editing user info'''
# data = requests.post(base_url + detail, data={'Authenticated': f'{TOKEN_vagran}'})

'''Catrgories'''
# data = requests.get(base_url + category, headers={'Content-type': 'application/json',  # headers!!!
#                                                    'Authorization': f'{TOKEN_vagran}',
#                                                    'email': 'vagvar@mail.ru',
#                                                    'password': 'sgers64$'})

'''Products'''
data = requests.get(base_url + products, headers={'Content-type': 'application/json',  # headers!!!
                                                  'Authorization': f'{TOKEN_vagran}',
                                                  'email': 'vagvar@mail.ru',
                                                  'password': 'sgers64$'})
print(data.url, data.status_code, data.request)
pprint(data.json())
