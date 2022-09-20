from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegistrationFormView.as_view(), name='register'),
    path('orders/', ProfileOrdersView.as_view(), name='orders'),
    path('orders/(?P<pk>)/$', ProfileOrderDetailView.as_view(), name='order_detail'),
    path('login/', AuthenticationForm.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileDetail.as_view(), name='detail'),
    path('profile/update/', UpdateProfileForm.as_view(), name='update'),
]