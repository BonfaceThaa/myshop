from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).exclude(deleted_at__isnull=False)
    best_sellers = Product.objects.filter(best_seller=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category).exclude(deleted_at__isnull=False)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'best_sellers': best_sellers
    })


def product_detail(request, id, slug):
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True
    )
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/cart_detail.html', {'product': product, 'cart_product_form': cart_product_form})


def custom_not_found(request, exception):
    return render(request, '404.html', status=404)




