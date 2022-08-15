from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from mycart.forms import CartAddProductForm
from .utils import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from candy_shop_app.models import Production, Category
from candy_shop_app.permissions import IsAdminOrReadOnly
from candy_shop_app.serializers import ProductionSerializer, CategorySerializer


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

class CandyShopAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductionAPIList(generics.ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CandyShopAPIListPagination


class ProductionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CandyShopAPIListPagination


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
