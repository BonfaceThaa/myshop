import factory
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import DynamicProvider

from django.utils.text import slugify

from shop.models import Product, Category

fake = Faker()

# TODO: confirm error in rendering categories html when using  Dynamic provider for category model


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.word()
    slug = slugify(name)


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    category = SubFactory(CategoryFactory)
    name = fake.word()
    slug = slugify(name)
    short_desc = fake.text(max_nb_chars=200)
    long_desc = fake.text(max_nb_chars=400)
    price = fake.pydecimal(left_digits=4, right_digits=2, positive=True)