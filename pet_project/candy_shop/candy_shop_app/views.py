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
