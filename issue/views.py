from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue
from .forms import IssueForm


# Create your views here.

@login_required()
def issue(request):
    if request.method == "POST":
        print("I am here in the issue method")
        issue_form = IssueForm(request.POST)

        if issue_form.is_valid():
            newissue = issue_form.save(commit=False)
            newissue.save()

            messages.error(request, "New issue has been created!")
            return redirect(reverse('issue'))
        else:
            print(issue_form.errors)
            messages.error(request, "Unable to submit issue!")
    else:
        issue_form = IssueForm()

    return render(request, "issue.html", {'issue_form': issue_form})
