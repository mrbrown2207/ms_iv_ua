from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from home.constants import FILTERS
from .models import Issue
from .forms import IssueForm


@login_required()
def issue(request):
    if request.method == "POST":
        issue_form = IssueForm(request.POST)

        if issue_form.is_valid():
            newissue = issue_form.save(commit=False)
            newissue.entered_by = request.user.first_name + ' ' + request.user.last_name
            newissue.entered_by_email = request.user.email
            newissue.save()

            messages.add_message(request, messages.SUCCESS, "New issue has been created!")
            return redirect(reverse('filters', args=(request.session['issue_filter'],)))

        print(issue_form.errors)
        messages.add_message(request, messages.ERROR, "Unable to submit issue!")
    else:
        current_user = request.user
        print(current_user)
        issue_form = IssueForm()

    return render(request, "issue.html", {'issue_form': issue_form})


def upvote(request, id):
    """Increase the upvote count"""
    i = get_object_or_404(Issue, pk=id)
    i.upvotes += 1
    i.save()

    # Take user back to main page, but ensure we maintain the filter state
    return redirect(reverse('filters', args=(request.session['issue_filter'],)))


def updissstatus(request, id):
    """
    Change the status. This will advance the status by one.
    So, if an issue has been reported and we come into this
    function, then it will then get promoted to "ongoing".
    If it is ongoing and we come in here, then will be promoted
    to "fixed". This could have easily been combined with the
    upvote function, but did this for complete clarity.
    """
    i = get_object_or_404(Issue, pk=id)

    # This should not happen, but check to make sure that we are
    # not here for an item with the wrong status. Also, make
    # sure the record doesn't already have a closed status. Again,
    # it shouldn't happen, but let's be safe.
    if i.status >= FILTERS.get('issues_closed'):
        messages.add_message(request, messages.ERROR, "Issue is already closed.")
    else:
        x = i.status + 1
        if x > FILTERS.get('issues_closed'):
            messages.add_message(request, messages.ERROR, "Action results in an invalid status.")
        else:
            i.status = x
            i.save()

    # Take user back to main page, but ensure we maintain the filter state
    return redirect(reverse('filters', args=(request.session['issue_filter'],)))
