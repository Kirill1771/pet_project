from django.urls import re_path, path, include
from . import views
from candy_shop_app.views import *

urlpatterns = [
    re_path(r'^category/(?P<category_slug>[-\w\d]+)/$', CategoryDetailView.as_view(), name='category'),
    re_path(r'^(?P<slug>[-\w\d]+)/$', ProductDetailView.as_view(), name='detail'),
    re_path(r'^$', ProductsListView.as_view(), name='index'),
    path('api/production', ProductionListAPI.as_view(), name='api_production_list'),
    path('api/category', CategoryListAPI.as_view(), name='api_category_list'),

]
