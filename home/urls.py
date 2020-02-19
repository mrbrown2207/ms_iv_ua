from django.conf.urls import url
from .views import index, filters

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^filters/(?P<filterid>\d+)', filters, name="filters"),
]
