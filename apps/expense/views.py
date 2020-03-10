from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db import IntegrityError
from django.shortcuts import render,  get_object_or_404, redirect
from django.http import (
    HttpResponseRedirect,
    HttpResponseNotFound
)
from django.db.models import Sum
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView

from core.mixins import StaffRequiredMixin

from apps.invoice.models import Invoice, Invoice_data

from .models import Expense
from .forms import ExpenseForm


@user_passes_test(lambda u: u.is_staff)
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, _('Expense was successfully Created!'))
            return redirect('expense:expense_list')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = ExpenseForm()

    context = {
        'form': form
    }
    return render(request, 'expense/expense_form.html', context)


@user_passes_test(lambda u: u.is_staff)
def expense_list(request):
    if request.user.username == 'Victor':
        object_list = Expense.objects.all().order_by('date', 'invoice_number')
        context = {
            'object_list': object_list,
            'edit': True
        }
    else:
        object_list = Expense.objects.filter(user=request.user).order_by('date', 'invoice_number')

        context = {
            'object_list': object_list,
            'edit': False
        }

    return render(request, 'expense/expense_list.html', context)


@user_passes_test(lambda u: u.is_staff)
def expense_update(request, pk):
    instance = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        if 'copy' in request.POST:
            form = ExpenseForm(request.POST, request.FILES)
        else:
            form = ExpenseForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, _('expense was successfully Update!'))
            return redirect('expense:expense_list')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = ExpenseForm(instance=instance)

    context = {
        'object': instance,
        'form': form,
        'update': True
    }
    return render(request,  'expense/expense_form.html', context)


@user_passes_test(lambda u: u.is_staff)
def expense_detail(request, pk):
    item = get_object_or_404(Invoice, pk=pk)
    data = Invoice_data.objects.filter(invoice__pk=item.pk)
    total = data.aggregate(sum=Sum('local_net'))
    total = total['sum']
    context = {
        'total': total,
        'item': item,
    }

    return render(request,  'expense/expense_detail.html', context)


class expense_delete(StaffRequiredMixin, DeleteView):

    model = Expense
    # por defecto busca MODEL_confirm_delete.html
    # template_name = 'settings/status_detete.html'
    success_url = reverse_lazy('expense:expense_list')

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            messages.success(request, _("Item {} deleted").format(self.object.invoice_number))
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except IntegrityError:
            return HttpResponseNotFound()

