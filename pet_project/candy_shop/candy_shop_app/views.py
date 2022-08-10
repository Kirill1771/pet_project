from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from mycart.forms import CartAddProductForm
from .utils import *


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Production.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  '#',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Production,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, '#', {'product': product,
                                 'cart_product_form': cart_product_form})
