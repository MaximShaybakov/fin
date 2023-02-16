import requests
from pprint import pprint

base_url = 'http://127.0.0.1:8000/api/v1/'

url_for_update = {"url": "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1K30Oeujse-05WCEGEFZC6oOX4Q_kACPy"}

us = {'update': 'partner/update/',
      'partner_state': 'partner/state/',
      'register': 'user/register/',
      'login': 'user/login/',
      'detail': 'user/details/',
      'category': 'categories/',
      'products': 'products/',
      'shops': 'shops/',
      'contacts': 'user/contact/'}

TOKEN_user1 = 'Token f50360db6c2e48baa4331124b90ec8863a37d772'
TOKEN_shop1 = 'Token 7a802a065d33b79c790072f37113752aab74ca63'

new_user = {'first_name': 'fn_user1',
            'last_name': 'ln_user1',
            'email': 'passw_user1@mail.ru',
            'password': 'hgj8756*&%$7',
            'company': 'yandex',
            'position': 'engineer',
            'is_superuser': True}

new_shop = {'first_name': 'fn_shop1',
            'last_name': 'ln_shop2',
            'email': 'mail_shop1@mail.ru',
            'password': 'passwd_shop1',
            'company': 'yandex',
            'position': 'market',
            'type': 'shop'}

'''User detail info '''
# data = requests.get(base_url + us['detail'],
#                     headers={'Content-type': 'application/json',  # headers!!!
#                              'Authorization': f'{TOKEN_user1}'},
#                     timeout=2)

# data = requests.post(base_url + us['detail'], headers={'Content-type': 'application/json',  # headers!!!
#                                                        'Authorization': f'{TOKEN_user1}'},
#                      json={'email': 'mail_user1@mail.ru'}, timeout=2)  # json!!!

'''User login'''
# data = requests.post(base_url + us['login'], data={'Content-type': 'application/json',  # DATA!!!
#                                                    'email': 'mail_shop1@mail.ru',
#                                                    'password': 'passwd_shop1'})

'''Register new user'''
# data = requests.post(base_url + us['register'], data=new_shop, timeout=3)  # data!!!

'''Catrgories'''
# data = requests.get(base_url + us['category'], headers={'Content-type': 'application/json',  # headers!!!
#                                                   'Authorization': f'{TOKEN_user1}'})

'''Products'''
# data = requests.get(base_url + us['products'], headers={'Content-type': 'application/json',  # headers!!!
#                                                   'Authorization': f'{TOKEN_user1}'})

'''Contact'''
# data = requests.get(base_url + us['contacts'], headers={'Content-type': 'application/json',  # headers!!!
#                                                   'Authorization': f'{TOKEN_user1}'})

'''Shops'''
# data = requests.get(base_url + us['shops'], headers={'Content-type': 'application/json',  # headers!!!
#                                                'Authorization': f'{TOKEN_user1}'})

# data = requests.delete(base_url + us['contacts'], headers={'Content-type': 'application/json',  # headers!!!
#                                                      'Authorization': f'{TOKEN_user1}'})

'''Partner state'''
# data = requests.get(base_url + us['partner_state'], headers={'Content-type': 'application/json',  # headers!!!
#                                                           'Authorization': f'{TOKEN_maxim}'})

'''Partner update'''
# data = requests.post(base_url + us['update'], headers={'Authorization': f'{TOKEN_vagran}'},
#                      data={"url": "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1K30Oeujse-05WCEGEFZC6oOX4Q_kACPy"})


print(data.url, data.status_code, data.request)
print(data.json())
