from django.utils.safestring import mark_safe
from django.template import Library

import simplejson as json


register = Library()


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj, use_decimal=True))