from django.shortcuts import render
from .constants import TABS, FILTERS

def filter_constants(request):
    """Make constants usable in templates"""
    return {
        'TAB_ISSUES': TABS.get('issues'),
        'TAB_FEATURES': TABS.get('features'),
        'ISSUES_ALL': FILTERS.get('issues_all'),
        'ISSUES_REPORTED': FILTERS.get('issues_reported'),
        'ISSUES_ONGOING': FILTERS.get('issues_ongoing'),
        'ISSUES_CLOSED': FILTERS.get('issues_closed'),
        'ISSUES_MINE': FILTERS.get('issues_mine'),
        'FEATURES_ALL': FILTERS.get('features_all'),
        'FEATURES_REQUESTED': FILTERS.get('features_requested'),
        'FEATURES_ACCEPTED': FILTERS.get('features_accepted'), # UA has accepted feature and awaits payment from requester
        'FEATURES_WORKING': FILTERS.get('features_working'), # Requester has paid
        'FEATURES_DECLINED': FILTERS.get('features_declined'),
        'FEATURES_FINISHED': FILTERS.get('features_finished'),
        'FEATURES_MINE': FILTERS.get('features_mine'),
    }
