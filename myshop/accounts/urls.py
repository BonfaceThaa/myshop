from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import register, account_profile, account_orders, account_order_details

app_name = 'accounts'

urlpatterns = [
    path('index/', account_profile, name='account_profile'),
    path('index/orders', account_orders, name='account_orders'),
    path('index/order/<str:order_id>', account_order_details, name='account_order_details'),
]