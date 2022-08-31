from django.urls import re_path
from .views import CheckoutOrderCreateView, OrderConfirmationView

urlpatterns = [
    re_path(r'^$', CheckoutOrderCreateView.as_view(), name='index'),
    re_path(r'confirmation/(?P<slug>[\w\d\-]+)/$',
            OrderConfirmationView.as_view(),
            name='order-confirmation'
            )
]
