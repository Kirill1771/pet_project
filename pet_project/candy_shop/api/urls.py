from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('production/', ProductionAPIList.as_view()),
    path('production/<slug:prod_slug>/', ProductionAPIUpdate.as_view()),
    path('productiondelete/<slug:prod_slug>/', ProductionAPIDestroy.as_view()),
    path('category/', CategoryAPIList.as_view()),
    path('category/<slug:cat_slug>/', CategoryAPIUpdate.as_view()),
    path('categorydelete/<slug:cat_slug>/', CategoryAPIDestroy.as_view()),

]
