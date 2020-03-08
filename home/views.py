from django.shortcuts import render
from django.db.models import Q
from issue.models import Issue
from feature.models import Feature
from .constants import TABS, FILTERS


def index(request):
    """
    A view that displays an index page showing a list of
    issues and features
    """
    request.session['issue_filter'] = FILTERS.get('issues_all')
    request.session['feature_filter'] = FILTERS.get('features_all')
    issues = Issue.objects.all().order_by('-date_added')
    features = Feature.objects.all().order_by('-date_added')
    current_tab = TABS.get('issues')

    return render(request, "index.html", {
        "issues":issues, "features":features,
        "current_tab":current_tab, "li":request.user.is_authenticated()
    })


def filters(request, filterid):
    """
    Filter what is displayed for issues and features. I am also preserving
    the state of the ui: what tab was the user on as well as what is their
    most recent filtering selection in both tabs (issues and features).
    """
    f_id = int(filterid)
    # Preserve the tab they are on so we can take them back there.
    if f_id < FILTERS.get('features_all'):
        current_tab = TABS.get('issues')
        request.session['issue_filter'] = f_id
    else:
        current_tab = TABS.get('features')
        request.session['feature_filter'] = f_id

    # Get the correct issue records based on filter selection
    if request.session['issue_filter'] == FILTERS.get('issues_all'):
        issues = Issue.objects.all().order_by('-date_added')
    elif request.session['issue_filter'] == FILTERS.get('issues_mine'):
        issues = Issue.objects.filter(entered_by_email=request.user.email).order_by('-date_added')
    else:
        issues = Issue.objects.all().filter(
            status=request.session['issue_filter']).order_by('-date_added')

    # Get the correct filter records based on filter selection
    if request.session['feature_filter'] == FILTERS.get('features_all'):
        features = Feature.objects.order_by('-date_added')
    elif request.session['feature_filter'] == FILTERS.get('features_mine'):
        features = Feature.objects.filter(entered_by_email=request.user.email).order_by('-date_added')
    else:
        # Accepted filter is slightly different because of the way I am
        # displaying in the UI.
        if request.session.get('feature_filter') == FILTERS.get('features_accepted'):
            features = Feature.objects.filter(Q(status=FILTERS.get('features_accepted'))|
                Q(status=FILTERS.get('features_working')))
        else:
            features = Feature.objects.filter(
                status=request.session['feature_filter']).order_by('-date_added')

    return render(request, "index.html", {
        "issues": issues, "features":features, "current_tab":current_tab, "li":request.user.is_authenticated()})
