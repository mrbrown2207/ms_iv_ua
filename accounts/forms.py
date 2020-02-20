from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from home.constants import NO_BOTS


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label="Email Address *",
        min_length=3, max_length=40,
        widget=forms.EmailInput(attrs={
            'class':'form-control required',
            'aria-describedby':'email address',
            'placeholder':'Enter email address',
        }),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'aria-describedby':'password',
            'placeholder':'Password'
        }))

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
            'placeholder':'Enter email address',
        }),
        required=True
    )

    password1 = forms.CharField(
        label="Password *",
        min_length=8, max_length=11,
        widget=forms.PasswordInput(attrs={
            'class':'form-control pwd required',
            'aria-describedby':'password',
            'placeholder':'Password (8 - 11 characters)',
        }),
        required=True
    )

    password2 = forms.CharField(
        label="Confirm Password *",
        min_length=8, max_length=11,
        widget=forms.PasswordInput(attrs={
            'class':'form-control pwd required',
            'aria-describedby':'repeat password',
            'placeholder':'Repeat password',
        }),
        required=True
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        #username = self.cleaned_data.get('username')
        if User.objects.filter(email=email):
            raise forms.ValidationError(u'Email address already used.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # This should not happen as JS should prevent us from getting to this
        # code until all required fields are entered.
        if not password1 or not password2:
            raise ValidationError("Password fields must not be empty")

        # Ditto. JS should not allow us to get here if passwords to not match.
        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

