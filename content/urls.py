from django.conf.urls import url
from .views import howitworks, about, contact


urlpatterns = [
    url(r'^$', howitworks, name='howitworks'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
]
