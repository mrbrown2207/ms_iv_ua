import json
from django.test import TestCase, Client
from django.urls import reverse
from home.constants import FILTERS
from feature.models import Feature
from issue.models import Issue


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.features_issues_url = reverse('index')
        self.filters_url = reverse('filters', args=['5'])

    def test_features_issues_GET(self):
        response = self.client.get(self.features_issues_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # <<<<<<<<<<---------- All Issues Permutations ---------->>>>>>>>>>
    def test_filters_all_issues_all_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_all')
        session['feature_filter'] = FILTERS.get('features_all')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_all_issues_requested_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_all')
        session['feature_filter'] = FILTERS.get('features_requested')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_all_issues_accepted_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_all')
        session['feature_filter'] = FILTERS.get('features_accepted')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_all_issues_declined_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_all')
        session['feature_filter'] = FILTERS.get('features_declined')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_all_issues_finished_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_all')
        session['feature_filter'] = FILTERS.get('features_finished')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # <<<<<<<<<<---------- Reported Issues Permutations ---------->>>>>>>>>>
    def test_filters_reported_issues_requested_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_reported')
        session['feature_filter'] = FILTERS.get('features_requested')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_reported_issues_accepted_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_reported')
        session['feature_filter'] = FILTERS.get('features_accepted')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_reported_issues_declined_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_reported')
        session['feature_filter'] = FILTERS.get('features_declined')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_reported_issues_finished_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_reported')
        session['feature_filter'] = FILTERS.get('features_finished')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # <<<<<<<<<<---------- Ongoing Issues Permutations ---------->>>>>>>>>>
    def test_filters_ongoing_issues_requested_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_ongoing')
        session['feature_filter'] = FILTERS.get('features_requested')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_ongoing_issues_accepted_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_ongoing')
        session['feature_filter'] = FILTERS.get('features_accepted')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_ongoing_issues_declined_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_ongoing')
        session['feature_filter'] = FILTERS.get('features_declined')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_ongoing_issues_finished_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_ongoing')
        session['feature_filter'] = FILTERS.get('features_finished')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # <<<<<<<<<<---------- Ongoing Issues Permutations ---------->>>>>>>>>>
    def test_filters_closed_issues_requested_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_closed')
        session['feature_filter'] = FILTERS.get('features_requested')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_closed_issues_accepted_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_closed')
        session['feature_filter'] = FILTERS.get('features_accepted')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_closed_issues_declined_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_closed')
        session['feature_filter'] = FILTERS.get('features_declined')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # <<<<<<<<<<---------- All Features Permutations ---------->>>>>>>>>>
    def test_filters_reported_issues_all_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_reported')
        session['feature_filter'] = FILTERS.get('features_all')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_ongoing_issues_all_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_ongoing')
        session['feature_filter'] = FILTERS.get('features_all')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_filters_closed_issues_all_features_GET(self):
        session = self.client.session
        session['issue_filter'] = FILTERS.get('issues_closed')
        session['feature_filter'] = FILTERS.get('features_all')
        session.save()
        response = self.client.get(self.filters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

