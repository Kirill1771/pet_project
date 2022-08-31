from django.urls import re_path, path

from .views import *

urlpatterns = [
    path('register/', RegistrationFormView.as_view(), name='register'),
    path('orders/', ProfileOrdersView.as_view(), name='orders'),
    re_path(r'^orders/(?P<pk>\d+)/$', ProfileOrderDetailView.as_view(), name='order_detail'),
    path('login/', AuthenticationForm.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileDetail.as_view(), name='detail'),
    path('profile/update/', UpdateProfileForm.as_view(), name='update'),
]