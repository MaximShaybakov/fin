import pytest
from user_data import USER_DATA, NEW_USER_DATA
from rest_framework import status
from fixtures import client, _url, _headers, _user, user_factory, category_factory, shop_factory
from orders.models import User


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
    response_unauth = client.post(path=f"{_url}user/details/", data=NEW_USER_DATA)
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




