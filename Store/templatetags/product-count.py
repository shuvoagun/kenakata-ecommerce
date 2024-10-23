from django import template
from Store.models import Product

register = template.Library()

@register.filter
def product_count():
    return 0