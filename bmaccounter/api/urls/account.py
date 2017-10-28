from django.conf.urls import url

from bmaccounter.api.views.account import (
    AccountCreateAPIView,
    AccountDeleteAPIView,
    AccountDetailAPIView,
    AccountListAPIView,
    AccountUpdateAPIView,
    FlaggedAccountListAPIView
)

urlpatterns = [
    url(r'^create/$', AccountCreateAPIView.as_view(), name='create_account'),
    url(r'^(?P<pk>\d+)/delete/$', AccountDeleteAPIView.as_view(), name='delete_account'),
    url(r'^(?P<pk>\d+)/$', AccountDetailAPIView.as_view(), name='detail_account'),
    url(r'^list/$', AccountListAPIView.as_view(), name='list_account'),
    url(r'^(?P<pk>\d+)/update/$', AccountUpdateAPIView.as_view(), name='update_account'),
    url(r'^flagged/list/$', FlaggedAccountListAPIView.as_view(), name='list_flagged_account'),
]
