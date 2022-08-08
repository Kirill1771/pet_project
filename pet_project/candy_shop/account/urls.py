from django.urls import re_path
from . import views
from django.contrib.auth.views import *

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^password-change/$', PasswordChangeView.as_view(),
            name='password_change'),
    re_path(r'^password-change/done/$', PasswordChangeDoneView.as_view(),
            name='password_change_done'),
    re_path(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password-reset/done/$', PasswordResetDoneView.as_view(),
            name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),
]