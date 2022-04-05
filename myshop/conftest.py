import pytest

from django.contrib.auth.models import User

from shop.models import Category, Product, ProductImage
from orders.models import Order


@pytest.fixture(autouse=True)
def use_custom_url_conf(settings):
    settings.ROOT_URLCONF = 'myshop.myshop.urls'


@pytest.fixture(scope='module')
def user_data():
    data = {
        'username': 'joshua',
        'password': 'Pidyash1'
    }
    return data


@pytest.fixture()
def admin_user(user_data, db):
    admin = User.objects.create_user(**user_data)
    return admin


@pytest.fixture()
def category_data():
    data = {
        "name": "Electronics",
        "slug": "electronics"
    }
    return data


@pytest.fixture()
def test_category(category_data):
    category = Category.objects.create(**category_data)
    return category


@pytest.fixture()
def product_data(test_category):
    data = {
        "category": test_category,
        "name": 'Portable Wireless Bluetooth Speakers',
        "slug": 'portable-wireless-bluetooth-speakers',
        "price": 699.00
    }
    return data


@pytest.fixture()
def test_product(product_data):
    product = Product.objects.create(**product_data)
    return product


@pytest.fixture()
def order_data():
    data = {
        "order_id": "1DVD2UY40L",
        "first_name": "Brian",
        "last_name": "Muturi",
        "email": "brian@muturi.com",
        "address": "Kasarani, Seasons",
        "postal_code": "09091",
        "city": "Nairobi",
        "created": "2022-02-07T08:01:09.035Z",
        "updated": "2022-02-18T07:00:53.778Z",
        "braintree_id": "",
        "discount": 0,
    }
    return data


@pytest.fixture()
def test_order(order_data):
    order = Order.objects.create(**order_data)
    return order
