from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('candy_shop_app.urls'), name='candy_shop'),
    re_path(r'^cart/', include('mycart.urls'), name='cart'),
]
