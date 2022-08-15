from django.urls import re_path, path, include
from . import views
from candy_shop_app.views import *

urlpatterns = [
    re_path(r'^$', views.product_list, name='production_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list,
            name='production_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail,
            name='production_detail'),
    path('drf-auth/', include('rest_framework.urls')),
    path('api/production/', ProductionAPIList.as_view()),
    path('api/production/<slug:prod_slug>/', ProductionAPIUpdate.as_view()),
    path('api/productiondelete/<slug:prod_slug>/', ProductionAPIDestroy.as_view()),
    path('api/category/', CategoryAPIList.as_view()),
    path('api/category/<slug:cat_slug>/', CategoryAPIUpdate.as_view()),
    path('api/categorydelete/<slug:cat_slug>/', CategoryAPIDestroy.as_view()),

]
