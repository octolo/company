from django import template

from company import get_company_model

register = template.Library()
company_model = get_company_model()


@register.simple_tag(name='search_url')
def search_url(obj, country):
    return (
        obj.country_search_extend_url(country)
        if obj.id
        else obj.country_search_url(country)
    )
