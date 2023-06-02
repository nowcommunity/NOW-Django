from django import template
from api.utils.query_params import preserve_view_query_params

register = template.Library()

@register.simple_tag(takes_context=True)
def preserve_query_params(context, url):
	return preserve_view_query_params(context['view'], url, context['request'])
