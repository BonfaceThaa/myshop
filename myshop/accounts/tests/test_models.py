import pytest
import factory
from factory.django import DjangoModelFactory
from faker import Faker

from django.contrib.auth.models import User
from accounts.models import Profile, update_user_profile


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    # TODO: add username, password, email, first_name, last_nanme
# TODO: Add user profile factory


@factory.django.mute_signals(update_user_profile)
@pytest.mark.django_db
class TestUserModel:
    def test_create_user_success(self):
        pass


@factory.django.mute_signals(update_user_profile)
@pytest.mark.django_db
class TestProfileModel:

    def test_create_profile_success(self):
        pass
