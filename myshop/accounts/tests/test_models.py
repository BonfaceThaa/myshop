import pytest
import factory
from factory import RelatedFactory
from factory.django import DjangoModelFactory
from faker import Faker

from django.contrib.auth.models import User
from accounts.models import Profile, update_user_profile

fake = Faker()


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory('accounts.UserFactory', profile=None)
    phone_number = fake.phone_number()
    address = fake.street_address()
    postal_code = fake.postcode()
    city = fake.city()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fake.word()
    first_name = username
    last_name = fake.word()
    password = 'Hashpappi101'
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')


@pytest.mark.django_db
class TestProfileModel:
    def test_create_profile_success(self):
        user = RelatedFactory(UserFactory)
        profile = Profile.objects.get(user=user)
        assert User.objects.count() == 1
        assert Profile.objects.count() == 1
        assert f"{user.username}'s profile" == str(profile)
