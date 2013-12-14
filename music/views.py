# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from music.models import *
from datetime import date

def musics(request):
	albums = Album.objects.order_by('-id')[:10]
	songs = Song.objects.order_by('-id')
	feast_img = feast()
	return render_to_response("music_list.html", locals(), context_instance=RequestContext(request))

def music_detail(request,album_id):
	album = get_object_or_404(Album,pk=album_id)
	songs = Song.objects.filter(album=album)
	feast_img = feast()
	return render_to_response("music_detail.html",locals(),context_instance=RequestContext(request))

def feast():
	today = date.today()
	feasts = Feast.objects.order_by('-start_time')
	for f in feasts:
		if f.start_time.month == today.month:
			if f.start_time.day <= today.day:
				return f.cover.url
	return ''