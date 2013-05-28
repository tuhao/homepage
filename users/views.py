from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def login(request):
    return render_to_response('login.html')

def user_login(request):
    try:
        email = request.META['email']
        password = request.META['password']
    except KeyError:
        return render_to_response('error.html')
    return render_to_response('vote_list.html',context_instance=RequestContext(request))
