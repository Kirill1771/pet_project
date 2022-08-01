from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.product_list, name='production_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list,
            name='production_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail,
            name='production_detail'),
]
