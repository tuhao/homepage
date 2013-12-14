from django.conf.urls import patterns,url
from views import *


urlpatterns = patterns('',
                       # blog
                       url(r'^$', blogs),
                       url(r'^blog/(?P<blog_id>\d+)/$', blog_detail),
                       url(r'^sort/(?P<sort_id>\d+)/$', sort_blogs),

                       url(r'^search/$',blog_search),

                       url(r'^about/$',about),
                       
                       )
