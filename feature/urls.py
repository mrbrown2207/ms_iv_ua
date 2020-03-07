from django.conf.urls import url
from .views import feature, updstatus


urlpatterns = [
    url(r'^$', feature, name="feature"),
    url(r'^updstatus/(?P<id>\d+)/(?P<status>\d+)', updstatus, name="updstatus"),
]
