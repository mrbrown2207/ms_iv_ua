from django import template

register = template.Library()

@register.simple_tag
def nameconcat(first_name, surname):
    """Concat first and surnames. To be safe, casting to string first."""
    return str(first_name) + ' ' + str(surname)