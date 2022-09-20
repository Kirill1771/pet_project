from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, TemplateView
from candy_shop_app.models import Production
from .forms import AddToCartForm
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CartItem
from .utils import get_cart
from . import serializers


class CartView(TemplateView):
    template_name = "#"

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)

        cart = get_cart(self.request)

        items = []
        if cart:
            items = cart.items.select_related('product__image')

        context.update({
            'cart': cart,
            'cart_items': items
        })

        return context


class RemoveCartItemView(DeleteView):
    """Удаление элемента из корзины"""
    model = CartItem
    success_url = reverse_lazy('cart:index')
    success_message = "The item has been deleted from your cart."
    http_method_names = ['post']

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RemoveCartItemView, self).delete(self.request, *args, **kwargs)

    def get_object(self, *args, **kwargs):
        cart = get_cart(self.request)
        return CartItem.objects.get(cart=cart, product_id=self.kwargs['product_id'])


class UpdateCartItemView(FormView):
    """Обновление элемента в корзине"""
    http_method_names = ['post']
    success_url = reverse_lazy('cart:index')
    form_class = AddToCartForm
    template_name = '#'
    context_object_name = 'cart'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        cart = get_cart(request)
        cart_item = CartItem.objects.get(cart=cart, pk=self.kwargs['pk'])
        cart_item.quantity = request.POST['cart_item_quantity']
        cart_item.save()
        return self.form_valid(form)

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, "Product quantity has been updated.")
        return super(UpdateCartItemView, self).form_valid(form)


class AddToCartView(FormView):
    """Добавление элемента в корзину"""
    template_name = '#'
    success_url = reverse_lazy('cart:index')
    http_method_names = ['post']
    form_class = AddToCartForm

    def form_valid(self, form, *args, **kwargs):
        product = get_object_or_404(Production, pk=self.kwargs['product_id'])
        quantity = form.cleaned_data['quantity']

        cart = get_cart(self.request, create=True)
        cart_item, cart_item_created = CartItem.objects.update_or_create(cart=cart, product=product)

        if cart_item_created is False:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return super(AddToCartView, self).form_valid(form)


class CartDetailView(APIView):
    """API Информация о продукции в корзине"""
    def get(self, request):
        cart = get_cart(request)
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)


class CartUpdateDeleteView(APIView):
    """API обновление/удаление продукции в корзине"""
    def get_object(self, id):
        try:
            cart = get_cart(self.request)
            return cart.items.get(pk=id)
        except CartItem.DoesNotExist:
            raise Http404

    def patch(self, request, id, *args, **kwargs):
        item = self.get_object(id)
        serializer = serializers.CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, id):
        item = self.get_object(id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
