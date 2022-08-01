from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class AddProductionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
        self.fields['name_package'].empty_label = "Вариант упаковки не выбран"

    class Meta:
        model = Production
        fields = ['name_prod', 'slug', 'compound', 'photo', 'cat', 'price']
        widgets = {
            'name_prod': forms.TextInput(attrs={'class': 'form-input'}),
            'compound': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'photo': forms.ImageField(),
            'cat': forms.ModelChoiceField(
                queryset=Category.objects.values_list('name', flat=True).distinct()),
            'price': forms.IntegerField(attrs={'class': 'form-input'}),
        }

    def clean_name_prod(self):
        name_prod = self.cleaned_data['name_prod']
        if len(name_prod) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return name_prod


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']