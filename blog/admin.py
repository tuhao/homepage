from django.contrib import admin
from blog.models import *

admin.site.register(Sort)

class BlogAdmin(admin.ModelAdmin):
	list_display = ('id','title','sort','pub_date','tags')
	class Media:
		js = (
		'/tinymce/tinymce.min.js',
		'/tinymce/config.js',)

admin.site.register(Blog,BlogAdmin)

class AboutAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	class Media:
		js = (
		'/tinymce/tinymce.min.js',
		'/tinymce/config.js',)

admin.site.register(About,AboutAdmin)
