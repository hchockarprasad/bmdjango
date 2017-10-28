from django.conf.urls import url, include


urlpatterns = [
    url(r'^account/', include("bmaccounter.api.urls.account", namespace='account-api')),
]
