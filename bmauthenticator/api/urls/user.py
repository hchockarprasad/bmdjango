from django.conf.urls import url

from bmauthenticator.api.views.user import (
    UserLoginAPIView,
    UserRegisterAPIView,
    UserUpdateAPIView,
)

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='user_login'),
    url(r'^register/$', UserRegisterAPIView.as_view(), name='user_register'),
    url(r'^update/$', UserUpdateAPIView.as_view(), name='user_update'),
]
