from django import template
from ..constants import *

register = template.Library()

@register.simple_tag
def show_class(tab, filter_type, current_filter):
    if filter_type == current_filter:
        return "active"
    else:
        return ""
