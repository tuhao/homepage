from django import template
import re

register = template.Library()

@register.filter()
def nbsp(str):
	tag = re.compile(r'&nbsp;')
	return tag.sub("", str)