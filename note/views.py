# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog,Sort
from django.contrib import auth
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
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
           return  HttpResponseRedirect(reverse('note.views.add'))
       else:
           message.append('username or password not correct')
   else:
       user = request.session.get('user', None)
       if user and user.is_authenticated():
           return HttpResponseRedirect(reverse('note.views.add'))
   return render_to_response('login.html', {'username': username, 'message': ''.join(message)}, context_instance=RequestContext(request))


def logout(request):
   auth.logout(request)
   request.session['user'] = None
   return render_to_response('login.html', context_instance=RequestContext(request))



@login_required
def add(request):
  if request.method == 'POST':
    form = MarkdownForm(data=request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      sort = Sort.objects.get(id=cd['sort_id'])
      new_blog = Blog.objects.create(sort=sort, title=cd['blog_title'], content=cd['blog_content'], tags=cd['blog_tags'])
      new_blog.save()
      message = 'success'
    else:
      sort_id = request.POST.get('sort_id')
      blog_title = request.POST.get('blog_title')
      blog_tags = request.POST.get('blog_tags')
      blog_content = request.POST.get('blog_content')
      message = form.errors
  sorts = Sort.objects.all()
  return render_to_response("note_add.html",locals(),context_instance=RequestContext(request))
			

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
