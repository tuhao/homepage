from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from users.models import *
#from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render_to_response('index.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




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
        try:
            name = request.POST.get('name', None)
            new_record = Record.objects.create(
                poll=poll, ip=ip, choise=selected_choise, name=name)
        except Exception, e:
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
