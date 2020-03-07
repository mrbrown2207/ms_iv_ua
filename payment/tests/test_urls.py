from django.test import SimpleTestCase
from django.urls import reverse, resolve
from payment.views import makepayment, paymentdetails


class TestUrls(SimpleTestCase):

    def test_makepayment_url_resolves(self):
        url = reverse('makepayment')
        print(resolve(url))
        self.assertEquals(resolve(url).func, makepayment)

    def test_paymentdetails_url_resolves(self):
        url = reverse('paymentdetails', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, paymentdetails)
