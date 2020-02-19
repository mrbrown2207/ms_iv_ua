import random
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from home.constants import NO_BOTS
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Create your views here.

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

        """Check to see if that email address already exists"""
        if user:
            auth.login(request, user)
            messages.error(request, "There is already an account with that email address.")
    else:
        """
        Generate a random question that helps to prevent robots from creating accounts.
        In the real world the result stored in the session would be encrypted and
        then decrypted when verifying.
        """
        no_bot_q, request.session['_asdf_'] = random.choice(list(NO_BOTS.items()))
        return render(request, 'register.html', {"no_bot_q":no_bot_q})

    #args = {'user_form': user_form}
    return render(request, 'register.html')
