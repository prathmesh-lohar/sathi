# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='custom_filter')
def custom_filter(value):
    # Your logic to manipulate the value
    # For example, let's say you want to capitalize the value
    return value.capitalize()
