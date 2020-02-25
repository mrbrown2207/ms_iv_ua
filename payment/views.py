from django.shortcuts import render, redirect, reverse
from .forms import PersonDetailsForm, CCDetailsForm

# Create your views here.
def paymentdetails(request):
    """A view that manages the payment details form"""
    person_details_form = PersonDetailsForm()
    cc_details_form = CCDetailsForm()

    args = {'person_details_form': person_details_form, 'cc_details_form': cc_details_form}
    return render(request, 'payment.html', args)


def makepayment(request, id):
    """Make payment"""
    if request.method == 'POST':
        person_details_form = PersonDetailsForm(request.POST)
    
    return redirect(reverse('index'))