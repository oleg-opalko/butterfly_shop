from django.contrib import messages
from django.shortcuts import render, redirect

from contacts.models import ContactUs
from contacts.templates.forms import ContactForm


# Create your views here.

def contact(request):
    contact_us = ContactUs.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = ContactForm()
    context = {
        'contactForm': form,
        'contact_us': contact_us
    }

    return render(request, 'contacts.html', context)

