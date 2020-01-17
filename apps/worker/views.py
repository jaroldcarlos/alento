from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.utils.translation import ugettext as _
from django.contrib.admin.views.decorators import staff_member_required

from core.utils import create_random_string
from .forms import WorkerForm
from .models import Worker


# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request.POST)
        if login_form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth_login(request, user)
                next_path = request.GET.get('next')
                return redirect('dashboard:home')
            else:
                login_form = AuthenticationForm()
                messages.error(request, _('username and password are not correct'))
                return render(request, 'login.html', {
                    'login_form': login_form,
                })
    else:
        login_form = AuthenticationForm()
        next_path = request.GET.get('next')
        return render(request, 'login.html', {
            'login_form': login_form,
        })


class SignOutView(LogoutView):
    pass


@staff_member_required
def create_worker(request):
    if request.method == 'POST':

        worker_form = WorkerForm(request.POST, request.FILES)
        if worker_form.is_valid():

            worker = worker_form.save(commit=False)
            worker.active_status = True
            passwd = create_random_string(9)

            first_name = worker_form.cleaned_data['first_name']
            last_name = worker_form.cleaned_data['last_name']
            dni = worker_form.cleaned_data['dni']
            is_staff = worker_form.cleaned_data['is_staff']
            email = worker_form.cleaned_data['email']

            # create user for asign to worker
            user = User.objects.create_user(dni, email=email, password=passwd, first_name=first_name, last_name=last_name)
            # user is staff
            if is_staff:
                user.is_staff = True
                user.save()

            if user:
                worker.user = user
            # send email to worker with user and password
            try:
                worker.save()
            except:
                user.delete()

            try:
                subject_for_user = _("alento")
                message_for_user = _("Welcome to alento, your credentials are: user: ")+dni+_(" password: ")+passwd
                send_mail(subject_for_user, message_for_user, 'info@alento.com', [email])
            except BadHeaderError:
                return HttpResponse(_('Invalid header found.'))

            messages.success(request, _('worker was successfully created'))
            return redirect('dashboard:home')
        else:
            messages.error(request, _('please correct the error below'))
    else:
        worker_form = WorkerForm()

    context = {
        'worker_form': worker_form,
    }

    return render(request, 'dashboard/form/worker.html', context)


@staff_member_required
def list_worker(request):

    items = Worker.actives.all()

    context = {
        'items': items,
    }

    return render(request, 'dashboard/view/worker_list.html', context)
