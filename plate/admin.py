from django.contrib import admin
from plate.models import *

class PlateAdmin(admin.ModelAdmin):
	list_display = ('name','pic','sort')

admin.site.register(Plate,PlateAdmin)