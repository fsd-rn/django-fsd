from django import template

register = template.Library()

@register.filter(name='ding')
def ding(value, arg):
    """
    This cuts out all the values of the 'arg' from the string..!
    """
    return value.replace(arg, '')

# register.filter('ding', ding)
