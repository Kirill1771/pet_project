from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^create/$', views.order_create, name='order_create'),
]