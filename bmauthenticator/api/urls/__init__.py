from django.conf.urls import url, include


urlpatterns = [
    url(r'^user/', include("bmauthenticator.api.urls.user", namespace='users-api')),
]
