from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    print(pattern, request.path)
    if re.match(pattern, request.path):
        return 'active'
    else:
        return ''