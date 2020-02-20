from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from home.constants import NO_BOTS


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    New user registration form
    Note: username and email address will be the same
    """
    first_name = forms.CharField(
        label="First Name *",
        min_length=1, max_length=40,
        widget=forms.TextInput(attrs={
            'class':'form-control required alpha-only text-capitalize',
            'aria-describedby':'first name',
            'placeholder':'First name',
            }),
        required=True
    )
    
    last_name = forms.CharField(
        label="Surname *",
        min_length=1, max_length=40,
        widget=forms.TextInput(attrs={
            'class':'form-control required alpha-only text-capitalize',
            'aria-describedby':'surname',
            'placeholder':'Surname',
            }),
        required=True
    )

    # According to IETF, minimum email address is 3 characters: x@x
    # Yes, maxlength is 254, but limiting to 40 for this assignment.
    email = forms.CharField(
        label="Email *",
        min_length=3, max_length=40,
        widget=forms.EmailInput(attrs={
            'class':'form-control required',
            'aria-describedby':'email address',
            'placeholder':'Email address',
        }),
        required=True
    )

    """
    pwd1 = forms.CharField(
        label="Password *",
        min_length=8, max_length=11,
        widget=forms.PasswordInput(attrs={
            'class':'form-control pwd required',
            'aria-describedby':'password',
            'placeholder':'Password (8 - 11 characters)',
        }),
        required=True
    )

    pwd2 = forms.CharField(
        label="Confirm Password *",
        min_length=8, max_length=11,
        widget=forms.PasswordInput(attrs={
            'class':'form-control pwd required',
            'aria-describedby':'repeat password',
            'placeholder':'Repeat password',
        }),
        required=True
    )
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        #username = self.cleaned_data.get('username')
        if User.objects.filter(email=email):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_pwd2(self):
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')

        # This should not happen as JS should prevent us from getting to this
        # code until all required fields are entered.
        if not pwd1 or not pwd2:
            raise ValidationError("Password must not be empty")

        # Ditto. JS should not allow us to get here if passwords to not match.
        if pwd1 != pwd2:
            raise ValidationError("Passwords do not match")

        return pwd2