from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db import IntegrityError
from django.shortcuts import render,  get_object_or_404, redirect
from django.http import (
    HttpResponseRedirect,
    HttpResponseNotFound
)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView

from core.mixins import StaffRequiredMixin

from apps.expense.models import Expense

from .models import Income
from .forms import IncomeForm

from webpush import send_group_notification

@user_passes_test(lambda u: u.is_staff)
def income_create(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, _('Income was successfully Created!'))
            return redirect('income:income_list')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = IncomeForm()

    context = {
        'form': form
    }

    payload = {'head': 'Welcome!', 'body': 'Hello World', 'icon': 'https://i.imgur.com/dRDxiCQ.png', 'url': 'https://www.example.com'}

    send_group_notification(user='admin', payload=payload, ttl=1000)

    return render(request, 'income/income_form.html', context)


@user_passes_test(lambda u: u.is_staff)
def income_list(request):
    expense_list = Expense.objects.all().order_by('date', 'invoice_number')
    income_list = Income.objects.all().order_by('date', 'invoice_number')

    context = {
        'expense_list': expense_list,
        'income_list': income_list,
    }
    return render(request, 'income/income_list.html', context)


@user_passes_test(lambda u: u.is_staff)
def income_update(request, pk):
    instance = get_object_or_404(Income, pk=pk)

    if request.method == 'POST':
        if 'copy' in request.POST:
            form = IncomeForm(request.POST, request.FILES)
        else:
            form = IncomeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, _('income was successfully Update!'))
            return redirect('income:income_list')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = IncomeForm(instance=instance)

    context = {
        'plugins': ['datepicker', ],
        'object': instance,
        'form': form,
        'update':True
    }
    return render(request,  'income/income_form.html', context)


class income_delete(StaffRequiredMixin, DeleteView):

    model = Income
    # por defecto busca MODEL_confirm_delete.html
    # template_name = 'settings/status_detete.html'
    success_url = reverse_lazy('income:income_list')

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            messages.success(request, _("Item {} deleted").format(self.object.invoice_number))
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except IntegrityError:
            return HttpResponseNotFound()
