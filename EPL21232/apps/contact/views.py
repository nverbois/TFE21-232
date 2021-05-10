import bleach
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from EPL21232 import settings
from .forms import ContactForm

# Bleach is an allowed-list-based HTML sanitizing library that escapes or strips markup and attributes.
# Bleach is intended for sanitizing text from untrusted sources.
# SMTP client SendGrid : 

def contact(request: HttpRequest) -> HttpResponse:
    print(settings.SENDGRID_API_KEY)
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid(): 
            name = bleach.clean(form.cleaned_data["nom"])
            email = bleach.clean(form.cleaned_data["email"])
            message = bleach.clean(form.cleaned_data["message"])
            send_mail(f"{name}, ({email}) a envoyé un email", message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL] )
            return render(request, "contact.html",{"form": form, "success": True})
    else:
        raise NotImplementedError
        
    return render(request, "contact.html",{"form": form})