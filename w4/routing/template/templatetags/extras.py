from django import template

register = template.Library()

@register.filter
def inc(value, param):
    return int(value) + int(param)
    
@register.simple_tag
def division(a, b, **kwargs):
    a = int(a)
    b = int(b)
    if 'to_int' in kwargs and kwargs['to_int']:
        return int(a / b)
    else:
        return a / b