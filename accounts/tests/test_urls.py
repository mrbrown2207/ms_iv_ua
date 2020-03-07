from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import login, userprofile, register, logout

class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_userprofile_url_resolves(self):
        url = reverse('userprofile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userprofile)

    def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout)

