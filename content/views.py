from django.shortcuts import render

# Create your views here.
def howitworks(request):
    """A view that displays the how it works page"""
    return render(request, "howitworks.html")

def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")

def contact(request):
    """A view that displays the contact us page"""
    return render(request, "contact.html")