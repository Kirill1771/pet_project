from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^', include('candy_shop_app.urls'), name='candy_shop'),
    path(r'^cart/', include('mycart.urls'), name='cart'),
    path(r'^orders/', include('orders.urls'), name='orders'),
    path(r'^account/', include('account.urls')),
]
