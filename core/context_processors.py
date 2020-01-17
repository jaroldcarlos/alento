from django.conf import settings
from django.utils.translation import ugettext as _
from apps.frontend.models import Link, Social


def layout_blocks(request):
    app_name = _("alento")
    try:
        menu_home = Link.objects.filter(hook='hf').get_descendants(include_self=False)
    except Link.DoesNotExist:
        menu_home = None

    try:
        menu_dash = Link.objects.filter(hook='hd').get_descendants(include_self=False)
    except Link.DoesNotExist:
        menu_dash = None

    try:
        socials = Social.actives.all()
    except Link.DoesNotExist:
        socials = None

    context = {
        'app_name': app_name,
        'home_frontend': menu_home,
        'dash': menu_dash,
        'socials': socials,
        'lang': request.LANGUAGE_CODE
    }

    return context


def setlanguage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES,
        'SELECTEDLANG': request.LANGUAGE_CODE
    }

    return context
