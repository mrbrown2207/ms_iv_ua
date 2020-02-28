import random
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserForm
from home.constants import NO_BOTS
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Profile


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, "You have successfully logged in. Welcome back " + user.first_name + "!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password are incorrect.")
    else:
        login_form = UserLoginForm()

    args = {'login_form': login_form}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if all((user_form.is_valid(), profile_form.is_valid())):
            # You need to pull out the first name and surname and update the user that way.
            new_user_info = user_form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = new_user_info
            user_profile.save()
    else:
        user = User.objects.get(username__exact=request.user.username)

        # This will populate our user form
        user_form = UserForm(instance=user)

        try:
            user_profile = user.userprofile.all()
        except user._meta.model.userprofile.RelatedObjectDoesNotExist:
            print('No profile found')
            user_profile = None

        profile_form = UserProfileForm(user_profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            # We need to check to ensure that the no bot validation
            # answer is correct. We have saved the answer in our session.
            if request.session['bota'] != request.POST.get("nobota"):
                if 'failed_bot_test_count' in request.session:
                    request.session['failed_bot_test_count'] += 1
                    if request.session['failed_bot_test_count'] == 5:
                        session_cleanup(request)
                        return redirect(reverse('index'))
                else:
                    request.session['failed_bot_test_count'] = 1

                # Display error message and generate new question
                messages.add_message(request, messages.ERROR, "Robot test failed. Please try again.")
                gen_bot_test(request)
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
                    messages.add_message(request, messages.SUCCESS, "You have been successfully registered. Welcome to the UA community " + request.POST.get('first_name') + "!")
                    return redirect(reverse('index'))
    else:
        gen_bot_test(request)
        reg_form = UserRegistrationForm()

    args = {"reg_form":reg_form}
    return render(request, 'register.html', args)


def session_cleanup(request):
    """Cleanup some session variables"""
    del request.session['bota']
    del request.session['botq']
    if 'failed_bot_test_count' in request.session:
        del request.session['failed_bot_test_count']


def gen_bot_test(request):
    """
    Generate a random question that helps to prevent robots from creating accounts.
    In the real world the result stored in the session would be encrypted and
    then decrypted when verifying.
    """
    request.session['botq'], request.session['bota'] = random.choice(list(NO_BOTS.items()))

