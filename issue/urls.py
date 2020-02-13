from django.conf.urls import url
from .views import issue


urlpatterns = [
    url(r'^$', issue, name="issue")
]
