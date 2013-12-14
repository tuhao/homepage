# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from music.models import *

def musics(request):
	albums = Album.objects.order_by('-id')
	return render_to_response("music_list.html", locals(), context_instance=RequestContext(request))

def music_detail(request,album_id):
	album = get_object_or_404(Album,pk=album_id)
	songs = Song.objects.filter(album=album)
	return render_to_response("music_detail.html",locals(),context_instance=RequestContext(request))