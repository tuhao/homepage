from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect,Http404
from users.forms import RegistForm
from users.models import *

# Create your views here.

def login(request):
    username = ''
    message = []
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = user
            return render_to_response('index.html',context_instance=RequestContext(request))
        else:
            message.append('username or password not correct')
    else:
        user = request.session.get('user',None)
        if user and user.is_authenticated():
            return render_to_response('index.html',context_instance=RequestContext(request))
    return render_to_response('login.html',{'username':username,'message': ''.join(message)},context_instance=RequestContext(request))
    

def logout(request):
    auth.logout(request)
    request.session['user'] = None
    return render_to_response('login.html',context_instance=RequestContext(request))

def regist(request):
    if request.method == 'POST':
        form = RegistForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            new_user.is_staff = False
            new_user.save()
            return render_to_response("login.html",{'username':cd['username']})
        else:
            return render_to_response("regist.html",{'username':request.POST.get('username'),'email':request.POST.get('email'),'message':form.errors},context_instance=RequestContext(request))
    return render_to_response("regist.html",context_instance=RequestContext(request))


def vote(request):
    polls = Poll.objects.order_by('-pub_date')[0:20]
    return render_to_response("vote.html",{'polls':polls},context_instance=RequestContext(request))

def poll(request,offset):
    choises = None
    poll = None
    if request.method == 'POST':
        choise_id = request['choise_group']
        
        return render_to_response("vote_detail.html",{'choise_id':choise_id},context_instance=RequestContext(request))
    else:
        try:
            poll_id = int(offset)
        except ValueError:
            raise Http404()
        else:
            choises = Choise.objects.filter(poll_id=poll_id)
            poll = Poll.objects.filter(id=poll_id)[0]
            polls = Poll.objects.order_by('-pub_date')[0:20]
            return render_to_response("vote_detail.html",{'choises':choises,'poll':poll,'polls':polls},context_instance=RequestContext(request))
    
