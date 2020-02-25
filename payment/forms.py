import datetime
from django import forms


class PersonDetailsForm(forms.Form):
    full_name = forms.CharField(
        label='Full Name *',
        min_length=5, max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only required text-capitalize',
            'aria-describedby':'full name',
            'placeholder':'Enter full name',
        }))

    addr_line1 = forms.CharField(
        label='Address Line 1 *',
        min_length=5, max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control required',
            'aria-describedby':'address line1',
            'placeholder':'Address line 1',
        }))

    addr_line2 = forms.CharField(
        label='Address Line 2',
        min_length=5, max_length=40,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'aria-describedby':'address line2',
            'placeholder':'Address line 2',
        }))

    addr_city = forms.CharField(
        label='Town or City *',
        min_length=5, max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only required',
            'aria-describedby':'town or city',
            'placeholder':'Town or city',
        }))

    addr_country = forms.CharField(
        label='County',
        min_length=5, max_length=40,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only',
            'aria-describedby':'county',
            'placeholder':'County',
        }))


class CCDetailsForm(forms.Form):
    now = datetime.datetime.now()

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(now.year, now.year+10)]

    """Setting required=False because stripe will be dealing with it???"""
    credit_card_number = forms.CharField(
        label='Credit Card Number *',
        required=False,
        min_length=16, max_length=16, # No AMEX
        widget=forms.TextInput(attrs={
            'class':'form-control numeric-only required',
            'aria-describedby':'credit card number',
            'placeholder':'Credit card number',
        }))

    cvv = forms.CharField(
        label='Security Code (CVV) *',
        required=False,
        min_length=3, max_length=3, # No AMEX
        widget=forms.TextInput(attrs={
            'class':'form-control numeric-only required',
            'aria-describedby':'cvv',
            'placeholder':'CVV',
        }))

    expiry_month = forms.ChoiceField(
        label='Month',
        choices=MONTH_CHOICES,
        required=False
    )

    expiry_year = forms.ChoiceField(
        label='Year',
        choices=YEAR_CHOICES,
        required=False
    )

    stripe_id = forms.CharField(widget=forms.HiddenInput)

