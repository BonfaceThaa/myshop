import pytest
from pytest_factoryboy import register
from faker import Faker

from django.contrib.auth.models import User

from shop.tests.factories import ProductFactory, CategoryFactory
from orders.tests.factories import OrderFactory, OrderItemFactory, OrderComplaintFactory
from orders.signals import id_generator

fake = Faker()

register(CategoryFactory)
register(ProductFactory)
register(OrderFactory)
register(OrderItemFactory)
register(OrderComplaintFactory)


@pytest.fixture(autouse=True)
def use_custom_url_conf(settings):
    settings.ROOT_URLCONF = 'myshop.myshop.urls'


@pytest.fixture(scope='module')
def user_data ():
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
def test_order():
    data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.free_email(),
        "address": fake.street_address(),
        "postal_code": fake.postcode(),
        "city": fake.city()
    }
    return data


@pytest.fixture()
def test_order_complaint():
    data = {
        "email": fake.free_email(),
        "message": fake.text(max_nb_chars=400)
    }
    return data
