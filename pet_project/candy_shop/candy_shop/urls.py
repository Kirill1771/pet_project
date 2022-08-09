from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('candy_shop_app.urls'), name='candy_shop'),
    re_path(r'^cart/', include('mycart.urls'), name='cart'),
    re_path(r'^orders/', include('orders.urls'), name='orders'),
    re_path(r'^account/', include('account.urls'), name='account'),
    re_path(r'^api/', include('api.urls'), name='api'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
