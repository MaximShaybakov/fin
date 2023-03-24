import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from orders.models import User, Category, Product, Shop


USER_DATA = {"first_name": "fn_test_user",
             "last_name": "ln_test_user",
             "email": "email_test_user@mail.ru",
             "password": "password_test_user*",
             "company": "company_test_user",
             "position": "position_test_user"}


@pytest.fixture
def shop_facrtory():
    def factory(*args, **kwargs):
        return baker.make(_model='Shop', *args, **kwargs)
    return factory


@pytest.fixture
def category_facrtory():
    def factory(*args, **kwargs):
        return baker.make(_model='Category', *args, **kwargs)
    return factory


@pytest.fixture
def _user():
    user = User.objects.create_user(**USER_DATA)
    return user


@pytest.fixture
def _headers(_user):
    token = Token.objects.create(user=_user)
    headers = {'HTTP_AUTHORIZATION': f'Token {token}'}
    return headers


@pytest.fixture
def user_factory():
    def factory(*args, **kwargs):
        return baker.make(_model='User', *args, **kwargs)
    return factory


@pytest.fixture
def _url():
    return "http://127.0.0.1:8000/api/v1/"


@pytest.fixture(autouse=True)
def client():
    return APIClient()


@pytest.mark.django_db
def test_register_account(client, _url, user_factory):
    count_users = User.objects.count()
    response = client.post(path=f"{_url}user/register/",
                           data=USER_DATA)
    data = response.json()
    assert response.status_code == 200
    assert data == {'Status': True}
    assert User.objects.count() == count_users + 1


@pytest.mark.django_db
def test_login_account(client, _url, _headers):
    response = client.post(path=f"{_url}user/login/", **USER_DATA)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_account_details(_url, client, _headers):
    response_unauth = client.get(path=f"{_url}user/details/")
    assert response_unauth.status_code == status.HTTP_403_FORBIDDEN

    response = client.get(path=f"{_url}user/details/", **_headers)
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert data['email'] == USER_DATA['email']
    # возврат пароля сериалайзер не обрабатывает поэтому не проверяется


@pytest.mark.django_db
def test_account_details_(_url, client, _headers):
    new_user_data = {"email": "email_user@mail.ru",
                     "password": "password_user",
                     "company": "company_user",
                     "position": "position_user"}

    response_unauth = client.post(path=f"{_url}user/details/", data=new_user_data)
    assert response_unauth.status_code == status.HTTP_403_FORBIDDEN

    client.credentials(**_headers)
    response = client.post(path=f"{_url}user/details/", data=new_user_data)
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert data['Data']['email'] == new_user_data['email']


@pytest.mark.django_db
def test_category_view(category_facrtory, _url, client, _headers):
    category = category_facrtory(_quantity=10)
    response = client.get(path=f'{_url}categories/')
    assert response.status_code == status.HTTP_403_FORBIDDEN

    client.credentials(**_headers)
    response = client.get(path=f'{_url}categories/')
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert data['count'] == len(category)


@pytest.mark.django_db
def test_product_info_view(_url, client, _headers):
    response = client.get(path=f'{_url}products/')
    assert response.status_code == status.HTTP_403_FORBIDDEN

    client.credentials(**_headers)
    response = client.get(path=f'{_url}products/')
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    # for index, prod in enumerate(data):
    #     prod['']




