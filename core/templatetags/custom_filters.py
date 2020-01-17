import locale
import re

from django import template
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe


locale.setlocale(locale.LC_ALL, '')
register = template.Library()


@register.inclusion_tag('inc/children.html')
def children(item):
    if item.pk:
        try:
            item = Link.objects.filter(pk=item.pk).get_descendants(include_self=False)
        except Link.DoesNotExist:
            item = ''

     context = {
        'item':item,
     }

     return context

@register.filter
def src_set(item, template="list"):
    if item:
        from django.template.loader import get_template
        context = {'item': item}
        template = get_template('filters/srcset_{}.html'.format(template))
        # template = Template(
        #     "<img srcset='"
        #         "{{ item.image.320w.url }} 320w, "
        #         "{{ item.image.480w.url }} 480w, "
        #         "{{ item.image.778w.url }} 778w' "
        #     "sizes='"
        #         "(max-width: 320px) 280px, "
        #         "(max-width: 480px) 440px,778px' "
        #     "src='{{ item.image.url }}' alt='{{ item.name }}'>"
        # )

        return mark_safe(template.render(context))


@register.filter(is_safe=True)
def mark(element, text):
    if text is not '':
        regex = re.compile(re.escape(text), re.IGNORECASE)
        element = regex.sub(
            "<span class='marked-text'>{}</span>".format(text),
            element
        )
#    element = element.replace(
#        text,
#        "<span class='marked-text'>{}</span>".format(text)
#    )
    return element


@register.filter
def pdb(element):
    import pdb
    pdb.set_trace()
    return element


@register.filter
def lookup(d, key):
    return d[key]


@register.filter
def currency(value):
    if not value:
        value = 0
    return '{} €'.format(
        locale.currency(value, symbol=False, grouping=True)
    )


@register.filter
def get_month(obj, month):
    return obj.month(month)

@register.filter(is_safe=True)
def graphic(value):
    if value:
        return mark_safe('<span class="glyphicon glyphicon-ok font-green"></span>')
    else:
        return mark_safe('<span class="glyphicon glyphicon-remove font-red"></span>')



@register.filter(is_safe=True)
def markdown(value):
    return mark_safe('<span class="markdown">'+markdownify(value)+'</span>')


@register.filter(is_safe=True)
def isdigit(value):
    return "{}".format(value).isdigit()


@register.filter(name='get_type', is_safe=False)
def get_type(value):
    t = type(value)
    return t.__module__ + "." + t.__name__


@register.filter()
def link(value, variant=None):

    if variant == 'phone':
        url = value

        for ch in ['(', ')', ' ']:
            url.replace(ch,'')

        if '+' in url:
            url.replace('+', '00')

        url = '0034' + url if not '00' in url[0:2] else url

        return mark_safe('<a href="tel:{}">{}</a>'.format(url, value))

    elif variant=='email':
        return mark_safe('<a href="mailto:{}">{}</a>'.format(value, value))

    elif variant=='http':
        return mark_safe('<a href="//{}">{}</a>'.format(value, value))

    elif variant=='blank':
        return mark_safe('<a href="{}" target="_BLANK">{}</a>'.format(value, value))

    else:
        return mark_safe('<a href="{}">{}</a>'.format(value, value))


@register.filter()
def iconify(value):
    if not value:
        return ""

    extension = str(value).split('.')[-1]
    icon = {
        'pdf':  'fa-file-pdf-o',
        'jpg':  'fa-file-photo-o',
        'haml': 'fa-file-code-o',
        'doc':  'fa-file-word-o',
        'docx': 'fa-file-word-o',
        'xlsx': 'fa-file-excel-o',
        'pptx': 'fa-file-powerpoint-o',
        'jpeg': 'fa-file-photo-o',
        'zip':  'fa-file-zip-o',
        'png':  'fa-file-photo-o',
        'mp3':  'fa-file-audio-o',
        'html': 'fa-file-code-o',
        'txt':  'fa-file-text-o',
    }
    return mark_safe(' <a href="{file}" title="{name}"><i class="fa {icon}"></i></a> '.format(
        name=value,
        file=value.url,
        icon=icon[extension]) if extension in icon.keys() else 'fa-file-pdf-o'
    )

@register.filter()
def password(value):
    if not value:
        return ""

    return mark_safe('******** <i class="fa fa-eye" title="{}"></i></a> '.format(value))

@register.filter(name='humanreadable', is_safe=True)
def human_readable_timedelta(value, complete=False):

    theDateAndTime = value
    fromDate = timezone.now()

    if theDateAndTime > fromDate:
        return None
    elif theDateAndTime == fromDate:
        return _('now')

    delta = fromDate - theDateAndTime

    deltaMinutes = delta.seconds // 60
    deltaHours = delta.seconds // 3600
    deltaYears = delta.days // 365
    deltaMonths = delta.days // 30
    deltaMinutes -= deltaHours * 60
    deltaWeeks = delta.days // 7
    deltaSeconds = delta.seconds - deltaMinutes * 60 - deltaHours * 3600
    deltaDays = delta.days - deltaWeeks * 7

    valuesAndNames = [
        (deltaYears, _('year')),
        (deltaMonths, _('month')),
        (deltaWeeks, _('week')),
        (deltaDays, _('day')),
        (deltaHours, _('hour')),
        (deltaMinutes, _('minute')),
        (deltaSeconds, _('second'))
    ]

    text = ""
    for value, name in valuesAndNames:
        if complete:
            if value > 0:
                text += len(text) and ", " or ""
                text += "%d %s" % (value, name)
                text += (value > 1) and "s" or ""
        else:
            if value > 0:
                text += "%d %s" % (value, name)
                text += (value > 1) and "s" or ""
                break

    # replacing last occurrence of a comma by an 'and'
    if text.find(",") > 0:
        text = " and ".join(text.rsplit(", ", 1))

    return text

@register.filter(name='page_filter')
def page_filter(self,items):
    current_value = items.number
    valmax = items.paginator.page_range[-1]
    gapval = 4
    valini = current_value-gapval

    if valini <=0:
        valini = 1

    valend = 1+current_value+gapval
    if valend > valmax:
        valend = valmax+1

    return range(valini, valend)



@register.filter('iso_to_date')
def iso_to_date(date_iso):
    return date_utils.iso_to_date(date_iso)


@register.filter('pretty_sql')
def pretty_sql(sql):
    try:
        sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
        return sql
    except Exception:
        return sql


@register.filter('pretty_json')
def pretty_json(json_text):
    try:
        pretty_json_text = json.dumps(json_text, indent=4)
        return pretty_json_text
    except Exception:
        return json_text


@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    if key:
        return dict_data.get(key)


@register.inclusion_tag('djutils/sort_th.html', takes_context=True)
def sort_th(context, sort_param_name, label):
    return {
        'is_current': context['sort_params'][sort_param_name]['is_current'],
        'is_reversed': context['sort_params'][sort_param_name]['is_reversed'],
        'url': context['sort_params'][sort_param_name]['url'],
        'label': label,
}

@register.filter(name='format')
def format(value, fmt):
    return fmt.format(value)


@register.filter(name='luck')
def luck(items, limit):
    return items[0:limit]


