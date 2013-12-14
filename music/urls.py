from django.conf.urls import patterns,url
from music.views import *

urlpatterns = patterns('',
		url(r'^$',musics),
		)