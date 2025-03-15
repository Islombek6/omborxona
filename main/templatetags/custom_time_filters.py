from django import template

register = template.Library()


@register.filter
def format_time(value):
    """Faqat soat va daqiqani chiqaradi"""
    if not value:
        return ""

    return value.strftime("%H:%M")  # Masalan: "14:30"
