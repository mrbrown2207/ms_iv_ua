import datetime
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from feature.models import Feature
from django.conf import settings
from home.constants import FILTERS
from .forms import PersonDetailsForm, CCDetailsForm

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def paymentdetails(request, id):
    """A view that manages the payment details form"""
    f = Feature.objects.get(id=id)

    person_details_form = PersonDetailsForm()
    cc_details_form = CCDetailsForm()

    args = {
        'person_details_form': person_details_form, 
        'cc_details_form': cc_details_form,
        'f_details': f,
        'publishable': settings.STRIPE_PUBLISHABLE
    }
    return render(request, 'payment.html', args)


def makepayment(request, id):
    """Make payment"""
    if request.method == 'POST':
        if 'submit' in request.POST:
            person_details_form = PersonDetailsForm(request.POST)
            cc_details_form = CCDetailsForm(request.POST)
            print(cc_details_form.is_valid())
            if cc_details_form.is_valid() == False:
                print("cc details form failed")
                print("****************** Form Errors *******************")
                print(cc_details_form.errors)
                print("*************** Non Field Errors *****************")
                print(cc_details_form.non_field_errors)
            if person_details_form.is_valid() and cc_details_form.is_valid():
                
                # Stripe code here #

                # Advance feature status
                feature = get_object_or_404(Feature, pk=id)
                feature.date_paid = datetime.datetime.now()
                feature.status = FILTERS.get('features_working')
                feature.save()
                messages.add_message(request, messages.SUCCESS, "Your payment was accepted. Thank you! We will start working immediately.")

    return redirect(reverse('index'))