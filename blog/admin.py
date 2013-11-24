from django.contrib import admin
from blog.models import *

admin.site.register(Sort)

class BlogAdmin(admin.ModelAdmin):
	list_display = ('id','title','sort','pub_date','tags')
	class Media:
		js = (
		'/static/tinymce/tinymce.min.js',
		'/static/tinymce/config.js',)

admin.site.register(Blog,BlogAdmin)

class AboutAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	class Media:
		js = (
		'/static/tinymce/tinymce.min.js',
		'/static/tinymce/config.js',)

admin.site.register(About,AboutAdmin)

admin.site.register(Link)
