import pytest
from pytest_factoryboy import register

from django.contrib.auth.models import User

from shop.tests.factories import ProductFactory, CategoryFactory
from orders.tests.factories import OrderFactory, OrderItemFactory, OrderComplaintFactory

register(CategoryFactory)
register(ProductFactory)
register(OrderFactory)
register(OrderItemFactory)
register(OrderComplaintFactory)


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
