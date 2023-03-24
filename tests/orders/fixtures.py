import pytest
from rest_framework.test import APIClient
from user_data import USER_DATA
from model_bakery import baker
from rest_framework.authtoken.models import Token
from orders.models import User


@pytest.fixture
def shop_factory():
    def factory(*args, **kwargs):
        return baker.make(_model='Shop', *args, **kwargs)
    return factory


@pytest.fixture
def category_factory():
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
