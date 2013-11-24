from django.conf.urls import patterns,url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from views import *

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'vote.views.home', name='home'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:

                       # blog
                       url(r'^$', blogs),
                       url(r'^blog/(?P<blog_id>\d+)/$', blog_detail),
                       url(r'^sort/(?P<sort_id>\d+)/$', sort_blogs),

                       url(r'^search/$',blog_search),

                       url(r'^about/$',about),
                       
                       )
