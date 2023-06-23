from django import template
register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
     return value * arg

@register.filter(name='remove_comilla')
def remove_quotes(value):
    return str(value).replace('"', '')