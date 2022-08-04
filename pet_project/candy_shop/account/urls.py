from django.urls import path
from . import views
from django.contrib.auth.views import *

urlpatterns = [
    path(r'^login/$', LoginView.as_view(), name='login'),
    path(r'^logout/$', LogoutView.as_view(), name='logout'),
    # path(r'^logout-then-login/$', include(logout_then_login()),
    #         name='logout_then_login'),
    path(r'^$', views.dashboard, name='dashboard'),
    path(r'^password-change/$', PasswordChangeView.as_view(),
            name='password_change'),
    path(r'^password-change/done/$', PasswordChangeDoneView.as_view(),
            name='password_change_done'),
    path(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    path(r'^password-reset/done/$', PasswordResetDoneView.as_view(),
            name='password_reset_done'),
    path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
    path(r'^register/$', views.register, name='register'),
    path(r'^edit/$', views.edit, name='edit'),
]