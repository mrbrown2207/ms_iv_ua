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
        no_bot_q = request.session['_asdf_']
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            # We need to check to ensure that the no bot validation
            # answer is correct. We have saved the answer in our session.
            if request.session['_asdf_'] != request.POST.get("no_bot_q"):
                if 'failed_bot_test_count' in request.session:
                    request.session['failed_bot_test_count'] += 1
                    if request.session['failed_bot_test_count'] == 5:
                        session_cleanup(request)
                        return redirect(reverse('index'))
                else:
                    request.session['failed_bot_test_count'] = 1

                # Display error message and generate new question
                messages.error(request, "Robot test failed. Please try again.")
                no_bot_q = gen_no_bot_q(request)
            else:
                # Have the username and email be the same. We only prompt for
                # email address at login
                reg_user = reg_form.save(commit=False)
                reg_user.username = request.POST.get('email')
                reg_user.save()

                session_cleanup(request)

                # Now let's authenticate the user and send them to main page.
                user = auth.authenticate(
                    username=request.POST.get('email'),
                    password=request.POST.get('password1'))

                if user:
                    auth.login(request, user)
                    messages.success(request, "You have been successfully registered!")
                    return redirect(reverse('index'))
    else:
        no_bot_q = gen_no_bot_q(request)
        reg_form = UserRegistrationForm()

    args = {"reg_form":reg_form, "no_bot_q":no_bot_q}
    return render(request, 'register.html', args)


def session_cleanup(request):
    """Cleanup some session variables"""
    del request.session['_asdf_']
    if 'failed_bot_test_count' in request.session:
        del request.session['failed_bot_test_count']

    return

def gen_no_bot_q(request):
    """
    Generate a random question that helps to prevent robots from creating accounts.
    In the real world the result stored in the session would be encrypted and
    then decrypted when verifying.
    """
    no_bot_q, request.session['_asdf_'] = random.choice(list(NO_BOTS.items()))

    return no_bot_q

