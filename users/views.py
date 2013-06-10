from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from users.forms import RegistForm
from users.models import *

#from django.contrib.auth.forms import UserCreationForm

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


def vote(request,poll_id):
    polls = Poll.objects.order_by('-pub_date')[0:20]
    poll = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choise = poll.choise_set.get(id=request.POST['choise'])
    except (KeyError,Choise.DoesNotExist):
        return render_to_response("vote_detail.html",{'poll':poll,'polls':polls,'error':'You must select a choise'},context_instance=RequestContext(request))
    else:
        selected_choise.votes += 1
        selected_choise.save()
        return HttpResponseRedirect(reverse('users.views.results',args=(poll.id,)))
    
def polls(request):
    polls = Poll.objects.order_by('-pub_date')[0:20]
    return render_to_response("vote_detail.html",{'polls':polls},context_instance=RequestContext(request))

def detail(request,poll_id):
    polls = Poll.objects.order_by('-pub_date')[0:20]
    poll = get_object_or_404(Poll,pk=poll_id)
    return render_to_response("vote_detail.html",{'polls':polls,'poll':poll},context_instance=RequestContext(request))

def results(request,poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    #polls = Poll.objects.order_by('-pub_date')[:20]
    return render_to_response("vote_result.html",{'poll':poll},context_instance=RequestContext(request))
