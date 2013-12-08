# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response

def music_list(request):
	
	 return render_to_response("music_list.html", locals(), context_instance=RequestContext(request))