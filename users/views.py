from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView

from cart.utils import get_cart
from orders.models import Order
from .forms import CustomUserRegistrationForm, CustomUserLoginForm
from .models import CustomUser


def profile_index(request):
    return render(request, "#")


class ProfileDetail(LoginRequiredMixin, DetailView):
    """Подробности профиля конкретного"""
    template_name = "#"
    login_url = reverse_lazy('profiles:login')
    model = CustomUser

    def get_object(self, queryset=None):
        return CustomUser.objects.get(pk=self.request.user.pk)


class RegistrationFormView(FormView):
    """Регистрация"""
    template_name = "#"
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        self.profile = form.save()
        self.request.session['user_cart'] = self.request.session.session_key

        user = authenticate(
            email=self.profile.email,
            password=self.request.POST['password1']
        )

        messages.add_message(
            self.request, messages.SUCCESS,
            'You were successfully logged in.'
        )

        login(self.request, user)
        return super(RegistrationFormView, self).form_valid(form)


class UpdateProfileForm(LoginRequiredMixin, UpdateView):
    """Изменение профиля"""
    template_name = '#'
    form_class = CustomUserRegistrationForm
    model = CustomUser
    success_url = reverse_lazy('homepage')
    login_url = reverse_lazy('profiles:login')

    def get_object(self, queryset=None):
        return CustomUser.objects.get(pk=self.request.user.pk)


class ProfileOrdersView(LoginRequiredMixin, ListView):
    """Заказы конкретного профиля"""
    model = Order
    template_name = '#'
    login_url = reverse_lazy('profiles:login')

    def get_context_data(self, **kwargs):
        context = super(ProfileOrdersView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user.id)

        return context


class ProfileOrderDetailView(LoginRequiredMixin, DetailView):
    """Подробности конкретного заказа конкретного профиля"""
    model = Order
    template_name = '#'
    login_url = reverse_lazy('profiles:login')


class AuthenticationForm(FormView):
    """Процесс аутентификации"""
    template_name = '#'
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):

        cart = get_cart(self.request, create=True)
        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])

        if user is not None and user.is_active:
            self.request.session['user_cart'] = self.request.session.session_key
            login(self.request, user)

            if cart is not None:
                cart.user = CustomUser.objects.get(id=user.id)
                cart.save()
                messages.add_message(self.request, messages.SUCCESS, 'You were successfully logged in.')

            return super(AuthenticationForm, self).form_valid(form)

        else:
            response = super(AuthenticationForm, self).form_invalid(form)
            messages.add_message(self.request, messages.WARNING, 'Wrong email or password. Please try again')
            return response


def logout_view(request):
    """Выход из системы"""
    logout(request)
    return HttpResponseRedirect('/')
