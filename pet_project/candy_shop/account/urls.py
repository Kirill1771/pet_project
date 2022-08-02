from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    re_path(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    re_path(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    re_path(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    re_path(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    re_path(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]