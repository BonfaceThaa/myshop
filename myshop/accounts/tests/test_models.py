import pytest
import factory
from factory import RelatedFactory
from factory.django import DjangoModelFactory
from faker import Faker

from django.contrib.auth.models import User
from accounts.models import Profile, update_user_profile

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fake.word()
    first_name = username
    last_name = fake.word()
    password = 'Hashpappi101'


@pytest.mark.django_db
class TestProfileModel:
    def test_create_profile_success(self):
        user = RelatedFactory()
        profile = Profile.objects.get(user=user)
        assert User.objects.count() == 1
        assert Profile.objects.count() == 1
        assert f"{user.username}'s profile" == str(profile)
