from django.urls import re_path, path

from .views import *

urlpatterns = [
    re_path(r'^$', CartView.as_view(), name='index'),
    re_path(r'^add/(?P<product_id>[0-9]+)/$', AddToCartView.as_view(), name='add'),
    re_path(r'^remove/(?P<product_id>[0-9]+)/$', RemoveCartItemView.as_view(), name='remove'),
    re_path(r'^update/(?P<pk>[0-9]+)/$', UpdateCartItemView.as_view(), name='update'),
    path('api/cart/', CartDetailView.as_view(), name='api_cart'),
    re_path(r'api/cart/(?P<id>[0-9]+)/$', CartUpdateDeleteView.as_view(), name='update_cart_api'),
]