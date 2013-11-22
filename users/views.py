from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
#from django import forms
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from users.forms import RegistForm
from users.models import *
#from django.contrib.auth.decorators import login_required

from users.blog import *

# Create your views here.


def index(request):
    return render_to_response('index.html')


#def login(request):
#    username = ''
#    message = []
#    if request.method == 'POST':
#        username = request.POST.get('username', '')
#        password = request.POST.get('password', '')
#        user = auth.authenticate(username=username, password=password)
#        if user is not None:
#            auth.login(request, user)
#            request.session['user'] = user
#            return render_to_response('index.html', context_instance=RequestContext(request))
#        else:
#            message.append('username or password not correct')
#    else:
#        user = request.session.get('user', None)
#        if user and user.is_authenticated():
#            return render_to_response('index.html', context_instance=RequestContext(request))
#    return render_to_response('login.html', {'username': username, 'message': ''.join(message)}, context_instance=RequestContext(request))

#
#def logout(request):
#    auth.logout(request)
#    request.session['user'] = None
#    return render_to_response('login.html', context_instance=RequestContext(request))


#def regist(request):
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
#    return render_to_response("regist.html", context_instance=RequestContext(request))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#@login_required


def vote(request, poll_id):
    polls = Poll.objects.order_by('-pub_date')
    #user = request.session.get("user", None)
    # if user is None:
    #    return HttpResponseRedirect(reverse('users.views.login'))
    ip = get_client_ip(request)
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choise = poll.choise_set.get(id=request.POST['choise'])
    except (KeyError, Choise.DoesNotExist):
        error = 'You must select a choise'
        return render_to_response("vote_detail.html", locals(), context_instance=RequestContext(request))
    else:
        #poll_record = Record.objects.filter(user=user, poll=poll)
        poll_record = Record.objects.filter(ip=ip, poll=poll)
        if poll_record:
            error = 'You had already made a choise'
            return render_to_response("vote_detail.html", locals(), context_instance=RequestContext(request))
        selected_choise.votes += 1
        selected_choise.save()
        #new_record = Record.objects.create(poll=poll, user=user, choise=selected_choise)
        new_record = Record.objects.create(
            poll=poll, ip=ip, choise=selected_choise)
        new_record.save()
        return HttpResponseRedirect(reverse('users.views.results', args=(poll.id,)))


def poll_detail(request, poll_id=1):
    polls = Poll.objects.order_by('-pub_date')
    try:
        poll = get_object_or_404(Poll, pk=poll_id)
    except Exception, e:
        pass
    return render_to_response("vote_detail.html", locals(), context_instance=RequestContext(request))


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll_records = Record.objects.filter(poll=poll)
    return render_to_response("vote_result.html", locals(), context_instance=RequestContext(request))
