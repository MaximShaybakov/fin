import requests
from pprint import pprint

base_url = 'http://127.0.0.1:8000/api/v1/'

us = {'update': 'partner/update/',
      'partner_state': 'partner/state/',
      'register': 'user/register/',
      'login': 'user/login/',
      'detail': 'user/details/',
      'category': 'categories/',
      'products': 'products/',
      'shops': 'shops/',
      'contacts': 'user/contact/'}

TOKEN_vasja = 'Token 33667d0bc49e1fea2d4396e0ee0e4934bcc93bb1'
TOKEN_vagran = 'Token f05313c2a9fcbf64ba2392b94110d95f3122257c'
TOKEN_maxim = 'Token 73843f8b6066517a836d659abd0c78ebd538a25d'
headers = {"email": "vasya-pupkin@mail.com", "password": "vasya-pupkin123"}

new_user = {'first_name': 'vagran',
            'last_name': 'vartanov',
            'email': 'vagvar@mail.ru',
            'password': 'sgers64$',
            'company': 'yandex',
            'position': 'engineer',
            'is_superuser': True}

new_shop = {'first_name': 'jorik',
            'last_name': 'vartanov',
            'email': 'jorvar@mail.ru',
            'password': 'jkhgci787ghj',
            'company': 'yandex',
            'position': 'ltd',
            'type': 'shop'}

'''User detail info '''
# data = requests.get(base_url + detail,
#                     headers={'Content-type': 'application/json',  # headers!!!
#                              'Authorization': f'{TOKEN_vagran}'},
#                     timeout=2)

'''User login'''
data = requests.post(base_url + us['login'], data={'Content-type': 'application/json',  # DATA!!!
                                                   'email': 'jorvar@mail.ru',
                                                   'password': 'jkhgci787ghj'})

'''Register new user'''
# data = requests.post(base_url + us['register'], data=new_user, timeout=3)  # data!!!

'''Editing user info'''
# data = requests.post(base_url + detail, data={'Authenticated': f'{TOKEN_vagran}'})

'''Catrgories'''
# data = requests.get(base_url + category, headers={'Content-type': 'application/json',  # headers!!!
#                                                   'Authorization': f'{TOKEN_vagran}'})

'''Products'''
# data = requests.get(base_url + products, headers={'Content-type': 'application/json',  # headers!!!
#                                                   'Authorization': f'{TOKEN_vagran}'})

'''Contact'''
# data = requests.get(base_url + contacts, headers={'Content-type': 'application/json',  # headers!!!
#                                                   'Authorization': f'{TOKEN_vagran}'})

'''Shops'''
# data = requests.get(base_url + shops, headers={'Content-type': 'application/json',  # headers!!!
#                                                'Authorization': f'{TOKEN_vagran}'})

# data = requests.delete(base_url + contacts, headers={'Content-type': 'application/json',  # headers!!!
#                                                      'Authorization': f'{TOKEN_vasja}'})

'''Partner state'''
# data = requests.get(base_url + us['partner_state'], headers={'Content-type': 'application/json',  # headers!!!
#                                                           'Authorization': f'{TOKEN_maxim}'})

# '''Partner update'''
# data = requests.post(base_url + us['update'])


print(data.url, data.status_code, data.request)
print(data.json())
