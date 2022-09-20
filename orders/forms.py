from django import forms

from .models import Address
from .models import Order


class ShippingAddressForm(forms.ModelForm):
    """Адрес доставки"""
    class Meta:
        model = Address
        fields = ['street', 'city', 'postcode', 'country']


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone']