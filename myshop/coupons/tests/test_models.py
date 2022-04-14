import pytest
import factory
from factory.django import DjangoModelFactory
from faker import Faker
from datetime import timedelta

from django.utils.timezone import make_aware

from coupons.models import Coupon

fake = Faker()


class CouponFactory(DjangoModelFactory):
    class Meta:
        model = Coupon

    code = factory.Sequence(lambda n: '%s' % fake.text(max_nb_chars=50))
    valid_from = make_aware(fake.date_time())
    valid_to = valid_from + timedelta(days=30)
    discount = fake.pyint(min_value=0, max_value=100)
    active = fake.pybool()


@pytest.mark.django_db
class TestCouponModel:

    def test_create_coupon_success(self):
        coupon = CouponFactory()
        assert Coupon.objects.count() == 1
        assert coupon.code == str(coupon)
