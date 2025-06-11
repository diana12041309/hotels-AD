from django import template

register = template.Library()

@register.filter
def cut_after_dot(value):
    """Returns text up to the first period (.)"""
    if not isinstance(value, str):
        return value
    return value.split('.')[0] + '.' if '.' in value else value
