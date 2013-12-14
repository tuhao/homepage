# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from music.models import *

def musics(request):
	songs = Song.objects.order_by('-id')
	return render_to_response("music_list.html", locals(), context_instance=RequestContext(request))