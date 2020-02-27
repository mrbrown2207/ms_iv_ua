from django.conf.urls import url
from .views import paymentdetails, makepayment


urlpatterns = [
    url(r'^(?P<id>\d+)', paymentdetails, name="paymentdetails"),
    url(r'^makepayment/', makepayment, name="makepayment"),
]
