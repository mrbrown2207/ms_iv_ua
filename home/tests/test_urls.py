from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, filters


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_filters_url_resolves(self):
        url = reverse('filters', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, filters)
