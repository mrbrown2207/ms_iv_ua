from django.conf.urls import url
from .views import paymentdetails, makepayment


urlpatterns = [
    url(r'^$', paymentdetails, name="paymentdetails"),
    url(r'^makepayment/(?P<id>\d+)', makepayment, name="makepayment"),
]
