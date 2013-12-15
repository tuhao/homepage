from django.conf.urls import patterns,url
from music.views import *

urlpatterns = patterns('',
		url(r'^$',musics),
		url(r'^album/(?P<album_id>\d+)/$',music_detail),
		)