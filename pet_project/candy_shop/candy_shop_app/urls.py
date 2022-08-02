from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.product_list, name='production_list'),
    path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list,
            name='production_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail,
            name='production_detail'),

]
