# import urllib
from django.utils.http import urlencode

from django import template

from goods.models import Products


register = template.Library()

@register.simple_tag()
def some_goods():
    return Products.objects.all()[:3]


@register.simple_tag(takes_context=True)
def compile_url(context, **kwargs):
    query = context['request'].GET.copy()

    for key, value in kwargs.items():
        if value is None:
            if key in query:
                del query[key]
        elif isinstance(value, list):
            query.setlist(key, value)
        else:
            query[key] = value

    # Возвращаем строку запроса без кавычек
    return f"?{query.urlencode()}" if query else ""