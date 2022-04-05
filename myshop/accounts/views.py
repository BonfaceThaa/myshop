import logging

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator

from .forms import RegisterForm, ProfileForm, UpdateUserForm
from orders.models import Order, OrderItem, OrderComplaint

logger = logging.getLogger(__name__)


def register(request):
    """
    Register a user and redirect to home page if successful.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def account_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(initial={}, instance=request.user.profile)
        user_form = UpdateUserForm(initial={}, instance=request.user)
    return render(request, 'profile/account_profile.html', {'profile_form': profile_form, "user_form": user_form})


def account_orders(request):
    orders = Order.objects.filter(customer=request.user)
    paginator = Paginator(orders, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'profile/account_orders.html', {'page_obj': page_obj})


def account_order_details(request, order_id):
    order = Order.objects.get(order_id=order_id)
    print("Order_item: ", order.created)
    order_items = order.items.all()
    context = {"order": order, "items": order_items}
    try:
        complaint = OrderComplaint.objects.get(order_id=order_id)
        context['complaint'] = complaint
    except ObjectDoesNotExist:
        pass
    return render(request, "profile/account_order_details.html", context)
