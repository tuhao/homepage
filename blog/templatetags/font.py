from django import template
import re

register = template.Library()


@register.filter()
def font(str, keyword):
    src = keyword
    font = re.compile(keyword, re.I)
    font_str = '%s%s%s' % ("<font style='color:red'>", src, "</font>")
    return font.sub(font_str, str)

