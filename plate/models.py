from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from blog.models import Blog

class Plate(models.Model):
	sort = models.ForeignKey(Blog)
	name = models.CharField(max_length=50)
	pic = models.ImageField(upload_to='upload/plates')
	pic_thumbnail = ImageSpecField(
		source='pic',
		processors=[ResizeToFill(190,145)],
		format='JPEG',
		options={'qulity':60}
		)
	description = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name