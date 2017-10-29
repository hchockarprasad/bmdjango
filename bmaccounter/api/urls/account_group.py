from django.conf.urls import url

from bmaccounter.api.views.account_group import (
    AccountGroupCreateAPIView,
    AccountGroupDeleteAPIView,
    AccountGroupDetailAPIView,
    AccountGroupListAPIView,
    AccountGroupUpdateAPIView,
)

urlpatterns = [
    url(r'^create/$', AccountGroupCreateAPIView.as_view(), name='create_account_group'),
    url(r'^(?P<pk>\d+)/delete/$', AccountGroupDeleteAPIView.as_view(), name='delete_account_group'),
    url(r'^(?P<pk>\d+)/$', AccountGroupDetailAPIView.as_view(), name='detail_account_group'),
    url(r'^list/$', AccountGroupListAPIView.as_view(), name='list_account_group'),
    url(r'^(?P<pk>\d+)/update/$', AccountGroupUpdateAPIView.as_view(), name='update_account_group'),
]
