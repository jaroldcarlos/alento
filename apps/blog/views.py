from django.contrib.admin.views.decorators import staff_member_required

from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from .models import BlogPost, BlogCategory
from .forms import BlogForm


def blog_index(request, category=None):

    try:
        categories = BlogCategory.actives.all()
    except BlogCategory.DoesNotExist:
        categories = ''

    try:
        items = BlogPost.actives.all()
    except BlogPost.DoesNotExist:
        items = ''

    if category:
        try:
            items = BlogPost.actives.filter(category__name=category)
        except BlogPost.DoesNotExist:
            items = ""

    context = {
        'items': items,
        'blog_categories': categories,
    }

    return render(request, 'blog/item.html', context)


@staff_member_required
def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.slug = slugify(blog.title)
            blog.date_active_ini = timezone.now()
            blog.date_active_end = timezone.now() + timezone.timedelta(days=365)
            blog.save()
            messages.success(request, _('blog was successfully created'))
            return redirect('dashboard:home')
        else:
            messages.error(request, _('please correct the error below.'))
    else:
        blog_form = BlogForm()

    context = {
        'blog_form': blog_form,
    }
    return render(request, 'dashboard/form/blog.html', context)


@staff_member_required
def list_blog(request, category=None):

    try:
        categories = BlogCategory.objects.all()
    except BlogCategory.DoesNotExist:
        categories = ''

    try:
        items = BlogPost.objects.all()
    except BlogPost.DoesNotExist:
        items = ''

    if category:
        try:
            items = BlogPost.objects.filter(category__name=category)
        except BlogPost.DoesNotExist:
            items = ""

    context = {
        'items': items,
        'blog_categories': categories,
    }

    return render(request, 'dashboard/view/blog_list.html', context)


def blog_post(request, slug):

    item = BlogPost.objects.get(slug_gl=slug)


    context = {
        'item': item,
    }

    return render(request, 'blog/blogpost.html', context)
