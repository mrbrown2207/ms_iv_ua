from django.conf.urls import url
from .views import feature


urlpatterns = [
    url(r'^$', feature, name="feature"),
]
