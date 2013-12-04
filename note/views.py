# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from note.forms import MarkdownForm

#from users.forms import RegistForm



def login(request):
   username = ''
   message = []
   if request.method == 'POST':
       username = request.POST.get('username', '')
       password = request.POST.get('password', '')
       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           request.session['user'] = user
           return render_to_response('note_add.html', context_instance=RequestContext(request))
       else:
           message.append('username or password not correct')
   else:
       user = request.session.get('user', None)
       if user and user.is_authenticated():
           return render_to_response('note_add.html', context_instance=RequestContext(request))
   return render_to_response('login.html', {'username': username,'message': ''.join(message)}, context_instance=RequestContext(request))


def logout(request):
   auth.logout(request)
   request.session['user'] = None
   return render_to_response('login.html',context_instance=RequestContext(request))

#def add(request):
#	if request.method == 'POST':
#		form = MarkdownForm(data = request.POST)
#		if form.is_valid():
#			cd = form.cleaned_data
#			sort = Sort.
#			new_blog = Blog.objects.create_blog(
#				sort=cd[''])

# def regist(request):
#    if request.method == 'POST':
#        form = RegistForm(data=request.POST)
#        if form.is_valid():
#            cd = form.cleaned_data
#            new_user = User.objects.create_user(
#                username=cd['username'], email=cd['email'], password=cd['password'])
#            new_user.is_staff = False
#            new_user.save()
#            return render_to_response("login.html", {'username': cd['username']})
#        else:
#            return render_to_response("regist.html", {'username': request.POST.get('username'), 'email': request.POST.get('email'), 'message': form.errors}, context_instance=RequestContext(request))
# return render_to_response("regist.html",
# context_instance=RequestContext(request))

#@login_required
