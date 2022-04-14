import random

import factory
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import DynamicProvider

from django.db.models.signals import pre_save

from orders.models import Order, OrderItem, OrderComplaint
from orders.signals import id_generator
from shop.tests.factories import ProductFactory

fake = Faker()

@factory.django.mute_signals(pre_save)
class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    # TODO: confirm how to pass instance to function used by signal while testing
    order_id = id_generator()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.free_email()
    address = fake.street_address()
    postal_code = fake.postcode()
    city = fake.city()


class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = SubFactory(OrderFactory)
    product = SubFactory(ProductFactory)
    price = factory.SelfAttribute('product.price')
    quantity = fake.random_digit()


class OrderComplaintFactory(DjangoModelFactory):
    class Meta:
        model = OrderComplaint

    order_id = SubFactory(OrderFactory)
    email = fake.free_email()
    message = fake.text(max_nb_chars=400)
