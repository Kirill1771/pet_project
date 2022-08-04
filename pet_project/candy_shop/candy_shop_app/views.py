from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from mycart.forms import CartAddProductForm

from .permissions import IsAdminOrReadOnly
from .serializers import CandyShopSerializer
from .utils import *


# class CandyShopHome(DataMixin, ListView):
#     model = Production
#     template_name = '#'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Главная страница")
#         return dict(list(context.items()) + list(c_def.items()))
#
#
# class ContactFormView(DataMixin, FormView):
#     form_class = ContactForm
#     template_name = '#'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Обратная связь")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return redirect('home')
#
#
# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Production.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Production,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


class CandyCategory(DataMixin, ListView):
    model = Production
    template_name = '#'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Production.objects.filter(
            cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


# class CandyAPIListPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
#
#
# class CandyAPIList(generics.ListCreateAPIView):
#     queryset = Production.objects.all()
#     serializer_class = CandyShopSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class = CandyAPIListPagination
#
#
# class CandyAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Production.objects.all()
#     serializer_class = CandyShopSerializer
#     permission_classes = (IsAuthenticated,)
#     # authentication_classes = (TokenAuthentication,)
#
#
# class CandyAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Production.objects.all()
#     serializer_class = CandyShopSerializer
#     permission_classes = (IsAdminOrReadOnly,)


def product_detail(request, id, slug):
    product = get_object_or_404(Production,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
