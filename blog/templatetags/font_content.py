from django import template
import re

register = template.Library()
@register.filter()
def font_content(str, keyword):
    less = len(keyword)
    key_group_str = r'[\s\S]{,20}' + keyword + r'[\s\S]{,50}'
    key_group_re = re.compile(key_group_str)
    result = ''
    font = re.compile(keyword)
    line_num = 0
    for m in key_group_re.finditer(str):
        line_num = line_num + 1
        if line_num > 3:
            break
        font_str = '%s%s%s' % ("<font style='color:red'>", keyword, "</font>")
        result = result + "..." + font.sub(font_str, m.group()) + "..."
    if line_num == 0:
        return str
    return result
