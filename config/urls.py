from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candy_shop_app.urls'), name='config'),
    path('cart/', include('mycart.urls'), name='cart'),
    path('orders/', include('orders.urls'), name='orders'),
    path('account/', include('account.urls'), name='account'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
