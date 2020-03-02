from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from home.constants import MIN_BID, MAX_BID
from .models import Feature
from .forms import FeatureForm

# Create your views here.

@login_required()
def feature(request):
    if request.method == "POST":
        feature_form = FeatureForm(request.POST)

        if feature_form.is_valid():
            newfeature_req = feature_form.save(commit=False)
            newfeature_req.entered_by = request.user.first_name + ' ' + request.user.last_name
            newfeature_req.entered_by_email = request.user.email
            newfeature_req.bid = request.POST.get('bid')
            newfeature_req.save()

            """
            Handled by the client
            if all((int(newfeature_req.bid) >= MIN_BID, int(newfeature_req.bid) <= MAX_BID)):
                newfeature_req.save()
            else:
                messages.add_message(request, messages.ERROR, "Bid must be between £10 and £5000.")
                return render(request, "feature.html", {'feature_form': feature_form})
            """

            messages.add_message(request, messages.SUCCESS, "New feature request has been created!")
            return redirect(reverse('filters', args=(request.session['feature_filter'],)))

        print(feature_form.errors)
        messages.add_message(request, messages.ERROR, "Unable to submit feature request!")
    else:
        feature_form = FeatureForm()

    return render(request, "feature.html", {'feature_form': feature_form})


def updstatus(request, id, status):
    """Change the status of the feature"""

    f = Feature.objects.get(id=id)
    f.status = int(status)
    f.save()

    # Take user back to main page, but ensure we maintain the filter state
    return redirect(reverse('filters', args=(request.session['feature_filter'],)))

