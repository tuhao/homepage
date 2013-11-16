from django.contrib import admin
from users.models import *

#admin.site.register(User)
admin.site.register(Poll)
admin.site.register(Choise)

class BlogAdmin(admin.ModelAdmin):
	list_display = ('id','title','pub_date')
	class Media:
		js = (
		'/tinymce/tinymce.min.js',
		'/tinymce/config.js',)

admin.site.register(Blog,BlogAdmin)