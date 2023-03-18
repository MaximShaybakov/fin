import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from orders.models import User


USER_DATA = {"first_name": "fn_user3",
             "last_name": "ln_user3",
             "email": "email_user3@mail.ru",
             "password": "kfJU*4d$#6",
             "company": "company_user3",
             "position": "position_user3"}


@pytest.fixture
def _user():
    user = User.objects.create_user(**USER_DATA)
    return user


@pytest.fixture
def _token(_user):
    token = Token.objects.create(user=_user)
    return token


@pytest.fixture
def url():
    return "http://127.0.0.1:8000/api/v1/"


@pytest.fixture(autouse=True)
def client():
    return APIClient()


@pytest.mark.django_db
def test_register_account(client, url):
    # post method
    count_users = User.objects.count()
    response = client.post(path=f"{url}user/register/",
                           data=USER_DATA)
    data = response.json()
    assert response.status_code == 200
    assert data == {'Status': True}
    assert User.objects.count() == count_users + 1


@pytest.mark.django_db
def test_login_account(client, url):
    # post method
    response = client.post(path=f"{url}user/login/",
                           data={'email': USER_DATA['email'], 'password': USER_DATA['password']})
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data['Status'] is True
