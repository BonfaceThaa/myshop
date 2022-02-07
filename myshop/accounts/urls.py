from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import register, profile, customer_orders

urlpatterns = [
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='/'), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/register', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', profile, name='profile'),
    path('index/orders', customer_orders, name='customer_orders')
]