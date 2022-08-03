from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'^login/$', LoginView.as_view(), name='login'),
    path(r'^logout/$', LogoutView.as_view(), name='logout'),
    path(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login',
            name='logout_then_login'),
    path(r'^$', views.dashboard, name='dashboard'),
    path(r'^password-change/$', 'django.contrib.auth.views.password_change',
            name='password_change'),
    path(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done',
            name='password_change_done'),
    path(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    path(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done',
            name='password_reset_done'),
    path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    path(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
            name='password_reset_complete'),
    path(r'^register/$', views.register, name='register'),
    path(r'^edit/$', views.edit, name='edit'),
]