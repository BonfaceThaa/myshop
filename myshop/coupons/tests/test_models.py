import pytest

from .factories import CouponFactory
from coupons.models import Coupon


@pytest.mark.django_db
class TestCouponModel:

    def test_create_coupon_success(self):
        coupon = CouponFactory()
        assert Coupon.objects.count() == 1
        assert coupon.code == str(coupon)

# TODO: test validators
