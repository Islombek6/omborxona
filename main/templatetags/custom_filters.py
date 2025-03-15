from django import template

register = template.Library()

OY_NOMLARI = {
    "January": "Yanvar", "February": "Fevral", "March": "Mart", "April": "Aprel",
    "May": "May", "June": "Iyun", "July": "Iyul", "August": "Avgust",
    "September": "Sentabr", "October": "Oktabr", "November": "Noyabr", "December": "Dekabr"
}

HAFTA_NOMLARI = {
    "Monday": "Dushanba", "Tuesday": "Seshanba", "Wednesday": "Chorshanba",
    "Thursday": "Payshanba", "Friday": "Juma", "Saturday": "Shanba", "Sunday": "Yakshanba"
}

@register.filter
def format_sana(value):
    """Sana va hafta kunlarini o‘zbek tiliga o‘giradi"""
    if not value:
        return ""
    sana_str = value.strftime("%A, %d %B %Y")  # "Friday, 08 March 2025"
    for en, uz in OY_NOMLARI.items():
        sana_str = sana_str.replace(en, uz)
    for en, uz in HAFTA_NOMLARI.items():
        sana_str = sana_str.replace(en, uz)
    return sana_str


