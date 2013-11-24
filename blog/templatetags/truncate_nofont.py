#from django import template
#import re
#
#register = template.Library()
#
#
#@register.filter()
#def truncate_nofont(str,length):
	#"""dont cut </font>"""
	#if len(str) < length:
		#return str
	#str = str[0:length]
	#font_str = r'</?\w*>?'
	#replace_str = '</font>'
    	#font_re = re.compile(font_str)
    	#return font_re.sub(replace_str, str)
    ##	return str


    

