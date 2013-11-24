from django import template
import re

register = template.Library()
@register.filter()
def font_content(str, keyword):
    less = len(keyword)
    key_group_str = r'[\s\S]{,50}' + keyword + r'[\s\S]{,50}'
    key_group_re = re.compile(key_group_str)
    result = ''
    font = re.compile(keyword)
    for m in key_group_re.finditer(str):
        font_str = '%s%s%s' % ("<font style='color:red'>", keyword, "</font>")
        result = result + "..." + font.sub(font_str, m.group()) + "..."
    return result