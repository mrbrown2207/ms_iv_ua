from django.shortcuts import render
from datetime import datetime
from issue.models import Issue
from feature.models import Feature
from .constants import *


def index(request):
    """
    A view that displays an index page showing a list of
    issues and features
    """
    request.session['issue_filter'] = ISSUES_ALL
    request.session['feature_filter'] = FEATURES_ALL
    issues = Issue.objects.all().order_by('-date_added')
    features = Feature.objects.all().order_by('-date_added')
    current_tab = ISSUES_TAB

    return render(request, "index.html", {
        "issues":issues, "features":features, "current_tab":current_tab, "li":request.user.is_authenticated()})


def filters(request, filterid):
    """Filter what is displayed for issues and features"""
    f_id = int(filterid)
    if f_id < FEATURES_ALL:
        current_tab = ISSUES_TAB
        request.session['issue_filter'] = f_id
    else:
        current_tab = FEATURES_TAB
        request.session['feature_filter'] = f_id

    if request.session['issue_filter'] == ISSUES_ALL:
        issues = Issue.objects.all().order_by('-date_added')
    else:
        issues = Issue.objects.all().filter(
            status=request.session['issue_filter']).order_by('-date_added')

    if request.session['feature_filter'] == FEATURES_ALL:
        features = Feature.objects.all().order_by('-date_added')
    else:
        features = Feature.objects.all().filter(
            status=request.session['feature_filter']).order_by('-date_added')

    return render(request, "index.html", {
        "issues": issues, "features":features, "current_tab":current_tab, "li":request.user.is_authenticated()})
