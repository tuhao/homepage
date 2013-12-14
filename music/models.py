from django.db import models
from django.conf import settings
from audiofield.fields import AudioField
import os.path
from django.utils.translation import ugettext_lazy as _

class Album(models.Model):
	name = models.CharField(max_length=50)
	cover = models.CharField(max_length=255)
	description = models.CharField(null=True,max_length=500)

	def __unicode__(self):
		return self.name

class Song(models.Model):
	album = models.ForeignKey(Album)
	name = models.CharField(max_length=50)
	created_date = models.DateTimeField('created time',auto_now_add=True)
	audio_file = AudioField(upload_to='upload/', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))
	lyc = models.TextField(u'lyc', max_length=1000, default='', blank=True)

	def audio_file_player(self):
    		"""audio player tag for admin"""
    		if self.audio_file:
        		file_url = settings.MEDIA_URL + str(self.audio_file)
        		player_string = '<ul class="playlist"><li style="width:250px;">\
        		<a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
        		return player_string
	audio_file_player.allow_tags = True
	audio_file_player.short_description = _('Audio file player')


	def __unicode__(self):
		return self.name
