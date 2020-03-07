from django.test import SimpleTestCase
from django.urls import reverse, resolve
from issue.views import issue, upvote, updissstatus


class TestUrls(SimpleTestCase):

    def test_issue_url_resolves(self):
        url = reverse('issue')
        print(resolve(url))
        self.assertEquals(resolve(url).func, issue)

    def test_upvote_url_resolves(self):
        url = reverse('upvote', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, upvote)

    def test_updissstatus_url_resolves(self):
        url = reverse('updissstatus', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, updissstatus)
