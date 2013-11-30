import xadmin
from models import UserSettings
from xadmin.layout import *
from blog.models import *
from vote import settings


class UserSettingsAdmin(object):
    model_icon = 'cog'
    hidden_menu = True
xadmin.site.register(UserSettings, UserSettingsAdmin)

xadmin.site.register(Sort)

#class BlogAdmin(xadmin.ModelAdmin):
#	list_display = ('id','title','sort','pub_date','tags')
#	class Media:
#		js = (
#		settings.STATIC_URL + 'tinymce/tinymce.min.js',
#		settings.STATIC_URL + 'tinymce/config.js',)
#
#xadmin.site.register(Blog,BlogAdmin)
#
#class AboutAdmin(xadmin.ModelAdmin):
#	list_display = ('id','title')
#	class Media:
#		js = (
#		settings.STATIC_URL + 'tinymce/tinymce.min.js',
#		settings.STATIC_URL + 'tinymce/config.js',)
#
#xadmin.site.register(About,AboutAdmin)
#
#xadmin.site.register(Link)