from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feature
from .forms import FeatureForm

# Create your views here.

@login_required()
def feature(request):
    if request.method == "POST":
        feature_form = FeatureForm(request.POST)

        if feature_form.is_valid():
            newfeature_req = feature_form.save(commit=False)
            newfeature_req.save()

            messages.error(request, "New feature request has been created!")
            return redirect(reverse('feature'))
        else:
            print(feature_form.errors)
            messages.error(request, "Unable to submit feature request!")
    else:
        feature_form = FeatureForm()

    return render(request, "feature.html", {'feature_form': feature_form})
