from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from .models import Contact_us

from apps.service.models import CategoryService, SpecialisedUnit


def home(request):
    try:
        service = CategoryService.objects.get(pk=1)
    except:
        service = ""

    eunit = SpecialisedUnit.objects.all()[:5]

    try:
        contact_us = Contact_us.objects.get(name='alento')
    except Contact_us.DoesNotExist:
        contact_us = None

    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        telephone = form.cleaned_data['telephone']
        from_email = form.cleaned_data['email']
        subject = "{name} {last_name} telf: {telephone}".format(
            name=name,
            last_name=last_name,
            telephone=telephone
        )
        message = form.cleaned_data['message']

        message_for_user = _("We will soon give you an answer to your message")
        subject_for_user = _("alento")

        try:
            send_mail(subject, message, from_email, ['info@alento.es'])
        except BadHeaderError:
            return HttpResponse(_('Invalid header found.'))
        try:
            send_mail(subject_for_user, message_for_user, 'info@alento.es', [from_email])
        except BadHeaderError:
            return HttpResponse(_('Invalid header found.'))
        return redirect('home')

    context = {
        'contact_us': contact_us,
        'form': form,
        'service': service,
        'eunit': eunit,
    }

    return render(request, 'frontend/index.html', context)


def contact(request):

    return render(request, 'pages/contact.html')
