from django import template
import re

register = template.Library()

def nbsp(str):
	tag = re.compile('&nbsp')
	return tag.sub(" ",str)

register.filter('nbsp',nbsp)