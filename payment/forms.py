import datetime
from django import forms
from django_countries.fields import CountryField


class PersonDetailsForm(forms.Form):
    full_name = forms.CharField(
        label='Card Holder Name *',
        min_length=5, max_length=40,
        required=False, # I am handling required
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only required text-capitalize',
            'aria-describedby':'full name',
            'placeholder':"Enter card holder's name",
        }))

    addr_line1 = forms.CharField(
        label='Address Line 1 *',
        min_length=5, max_length=40,
        required=False, # I am handling required
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
        required=False, # I am handling required
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only required text-capitalize',
            'aria-describedby':'town or city',
            'placeholder':'Town or city',
        }))

    addr_postcode = forms.CharField(
        label='Postcode *',
        min_length=5, max_length=8,
        required=False, # I am handling required
        widget=forms.TextInput(attrs={
            'class':'form-control required text-uppercase',
            'aria-describedby':'postcode',
            'placeholder':'Postcode',
        }))

    addr_country = CountryField().formfield(
        label='Country', initial='GB'
    )


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
            'placeholder':'0000 0000 0000 0000',
        }))

    cvv = forms.CharField(
        label='Security Code (CVV) *',
        required=False,
        min_length=3, max_length=3, # No AMEX
        widget=forms.TextInput(attrs={
            'class':'form-control numeric-only required short-input-field',
            'aria-describedby':'cvv',
            'placeholder':'CVV',
        }))

    expiry_month = forms.ChoiceField(
        label='Expires Month',
        choices=MONTH_CHOICES,
        initial=str(now.month),
        required=False,
        widget=forms.Select(attrs={
            'minlength': '2',
            'maxlength': '2',
            'class': 'short-input-field',
        }))

    expiry_year = forms.ChoiceField(
        label='Expires Year',
        choices=YEAR_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'minlength': '4',
            'maxlength': '4',
            'class': 'short-input-field',
        }))

    stripe_id = forms.CharField(widget=forms.HiddenInput)

