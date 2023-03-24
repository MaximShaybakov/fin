import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from orders.models import User
import ujson

USER_DATA = {"first_name": "fn_test_user",
             "last_name": "ln_test_user",
             "email": "email_test_user@mail.ru",
             "password": "password_test_user*",
             "company": "company_test_user",
             "position": "position_test_user"}


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
        return baker.make(User, *args, **kwargs)
    return factory


@pytest.fixture
def url():
    return "http://127.0.0.1:8000/api/v1/"


@pytest.fixture(autouse=True)
def client():
    return APIClient()


@pytest.mark.django_db
def test_register_account(client, url, user_factory):
    # post method
    # users = user_factory(_quantity=10)
    count_users = User.objects.count()
    response = client.post(path=f"{url}user/register/",
                           data=USER_DATA)
    data = response.json()
    assert response.status_code == 200
    assert data == {'Status': True}
    # assert len(data) == len(users)
    # for index, val in enumerate(data):
    #     assert val['email'] == users[i].email
    assert User.objects.count() == count_users + 1


@pytest.mark.django_db
def test_login_account(client, url, _headers):
    # post method
    response = client.post(path=f"{url}user/login/", **USER_DATA)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_account_details(url, client, _headers):
    # get method - get the data
    response_unauth = client.get(path=f"{url}user/details/")
    assert response_unauth.status_code == status.HTTP_403_FORBIDDEN
    response = client.get(path=f"{url}user/details/", **_headers)
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert data['email'] == USER_DATA['email']
    # возврат пароля сериалайзер не обрабатывает


@pytest.mark.django_db
def test_account_details_(url, client, _headers):
    # post method - partially change the data
    new_user_data = {"email": "email_user@mail.ru",
                     "password": "password_user",
                     "company": "company_user",
                     "position": "position_user"}

    response_unauth = client.post(path=f"{url}user/details/", data=new_user_data)
    assert response_unauth.status_code == status.HTTP_403_FORBIDDEN

    client.credentials(**_headers)
    response = client.post(path=f"{url}user/details/", data=new_user_data)
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert data['Data']['email'] == new_user_data['email']
