from django.conf.urls import url, include


urlpatterns = [
    url(r'^account/', include("bmaccounter.api.urls.account", namespace='account-api')),
    url(r'^account-group/', include("bmaccounter.api.urls.account_group", namespace='account-group-api')),
]
