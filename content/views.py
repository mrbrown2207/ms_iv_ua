from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def howitworks(request):
    """A view that displays the how it works page"""
    return render(request, "howitworks.html")

def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")

def contact(request):
    """A view that displays the contact us page"""
    # By default we do not want the submit button enabled until they
    # entered all required fields.
    enable_submit = False

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # Code would go here to send email to MBUA. For now, just display
            # a success message. Also note, that success message would most likely
            # be in a modal dialog in reality.

            messages.add_message(request, messages.SUCCESS, "Thank you for your message. Someone will be in contact within 48 hours.")
            return redirect(reverse('filters', args=(request.session['issue_filter'],)))
        else:
            # They have entered all the fields required, but something failed validation.
            # Leave submit button enabled so they don't have to re-enter all fields.
            enable_submit = True

    else:
        contact_form = ContactForm()

    return render(request, "contact.html", {'contact_form': contact_form, 'enable_submit': enable_submit})