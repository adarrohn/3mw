from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.match(pattern, request.path):
        return 'active'
    else:
        return ''