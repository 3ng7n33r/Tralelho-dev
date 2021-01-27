from django import template

register = template.Library()


@register.simple_tag
def exclude_base_language(Country, base_language):
    return Country.translated_spoken_languages(base_language)
