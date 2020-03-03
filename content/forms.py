from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    """Simple contact form"""

    phone_regx = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    first_name = forms.CharField(
        label='First Name *',
        min_length=5, max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only ua-required text-capitalize',
            'aria-describedby':'first name',
            'placeholder':"Enter first name",
        })
    )

    surname = forms.CharField(
        label='Surname *',
        min_length=5, max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control alpha-only ua-required text-capitalize',
            'aria-describedby':'Surname',
            'placeholder':'Surname',
        })
    )

    email_addr = forms.CharField(
        label='Email Address *',
        min_length=3, max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control ua-required text-lowercase',
            'aria-describedby':'email address',
            'placeholder':'Email address',
        })
    )

    phone = forms.CharField(
        label='Phone Number',
        min_length=5, max_length=19,
        validators=[phone_regx],
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'aria-describedby':'phone number',
            'placeholder':'Enter phone number',
        })
    )

    msg = forms.CharField(
        label='Message *',
        min_length=1, max_length=500,
        widget=forms.Textarea(attrs={
            'class':'form-control ua-required char-countdown',
            'aria-describedby':'your message',
            'placeholder':'Enter reason for contact',
            'cols':70, 'rows':8,
        })
    )
