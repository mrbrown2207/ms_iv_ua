from django.shortcuts import render
from datetime import datetime
from issue.models import Issue


# Create your views here.
def index(request):
    """A view that displays an index page"""
    issues = Issue.objects.all()

    return render(request, "index.html", {"issues": issues})
#    return render(request, "index1.html")

