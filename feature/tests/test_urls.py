from django.test import SimpleTestCase
from django.urls import reverse, resolve
from feature.views import feature, updstatus


class TestUrls(SimpleTestCase):

    def test_feature_url_resolves(self):
        url = reverse('feature')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feature)

    def test_updstatus_url_resolves(self):
        url = reverse('updstatus', args=['1', '1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, updstatus)
