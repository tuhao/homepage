from django.conf.urls import patterns,url
from note.views import *

urlpatterns = patterns('',
	url(r'^$',login),
	)