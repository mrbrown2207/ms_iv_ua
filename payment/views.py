import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from feature.models import Feature
from django.conf import settings
from django.utils import timezone
from home.constants import FILTERS, DEFAULT_CURRENCY
from .forms import PersonDetailsForm, CCDetailsForm

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def paymentdetails(request, id):
    """A view that manages the payment details form"""
    f = Feature.objects.get(id=id)

    person_details_form = PersonDetailsForm()
    cc_details_form = CCDetailsForm()

    request.session['active_feature_id'] = id

    args = {
        'person_details_form': person_details_form, 
        'cc_details_form': cc_details_form,
        'f_details': f,
        'publishable': settings.STRIPE_PUBLISHABLE
    }
    return render(request, 'payment.html', args)


def makepayment(request):
    """Make payment"""
    if request.method == 'POST':
        person_details_form = PersonDetailsForm(request.POST)
        cc_details_form = CCDetailsForm(request.POST)
        if person_details_form.is_valid() and cc_details_form.is_valid():
            feature = get_object_or_404(Feature, pk=request.session.get('active_feature_id', {}))
            try:
                customer = stripe.Charge.create(
                    amount=int(feature.bid * 100),
                    currency=DEFAULT_CURRENCY,
                    description=feature.entered_by,
                    card=cc_details_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.add_message(request, messages.ERROR, "Your card was declined!")

            if customer.paid:
                # Advance feature status
                feature.date_paid = timezone.now()
                feature.status = FILTERS.get('features_working')
                feature.save()
                messages.add_message(request, messages.SUCCESS, "Your payment was accepted. Thank you! We will start working immediately.")
        else:
            if cc_details_form.is_valid() == False:
                print("cc details form failed")
                print("****************** Form Errors *******************")
                print(cc_details_form.errors)
                print("*************** Non Field Errors *****************")
                print(cc_details_form.non_field_errors)
            else:
                print("person details form failed")
                print("****************** Form Errors *******************")
                print(person_details_form.errors)
                print("*************** Non Field Errors *****************")
                print(person_details_form.non_field_errors)

    return redirect(reverse('index'))