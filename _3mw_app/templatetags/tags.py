from django import template

register = template.Library()

@register.simple_tag
def active_basic(request, pattern):
    """
    Basic match anywhere in path
    """
    import re
    if re.match(pattern, request.path):
        return 'active'
    else:
        return ''

@register.simple_tag
def active_exact(request, pattern):
    """
    Only matches an exact path
    """
    import re
    if re.match(r'^{}/?$'.format(pattern), request.path):
        return 'active'
    else:
        return ''