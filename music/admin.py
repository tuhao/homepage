from music.models import *
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class SongAdmin(admin.ModelAdmin):
    """Allows the administrator to view and modify uploaded audio files"""
    list_display = ('id', 'name', 'audio_file_player', 'created_date', 'album')
    #list_display_links = ['id', 'name',]
    ordering = ('id', )

    actions = ['custom_delete_selected']

    def custom_delete_selected(self, request, queryset):
        #custom delete code
        n = queryset.count()
        for i in queryset:
            if i.audio_file:
                if os.path.exists(i.audio_file.path):
                    os.remove(i.audio_file.path)
            i.delete()
        self.message_user(request, _("Successfully deleted %d audio files.") % n)
    custom_delete_selected.short_description = "Delete selected items"

    def get_actions(self, request):
        actions = super(SongAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    class Media:
		js = (
		settings.STATIC_URL + 'tinymce/tinymce.min.js',
		settings.STATIC_URL + 'tinymce/config.js',)

admin.site.register(Song, SongAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    class Media:
        js = (
        settings.STATIC_URL + 'tinymce/tinymce.min.js',
        settings.STATIC_URL + 'tinymce/config.js',)

admin.site.register(Album,AlbumAdmin)

admin.site.register(Feast)
