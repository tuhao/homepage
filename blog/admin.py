from django.contrib import admin
from blog.models import *
from vote import settings

#from django_markdown.admin import MarkdownModelAdmin

#admin.site.register(Blog, MarkdownModelAdmin)

admin.site.register(Sort)

class BlogAdmin(admin.ModelAdmin):
	list_display = ('id','title','sort','pub_date','tags')
	class Media:
		js = (
		settings.STATIC_URL + 'tinymce/tinymce.min.js',
		settings.STATIC_URL + 'tinymce/config.js',)

admin.site.register(Blog,BlogAdmin)

class AboutAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	class Media:
		js = (
		settings.STATIC_URL + 'tinymce/tinymce.min.js',
		settings.STATIC_URL + 'tinymce/config.js',)

admin.site.register(About,AboutAdmin)

admin.site.register(Link)
