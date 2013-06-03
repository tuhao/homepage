from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from users.views import *
import os.path

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vote.views.home', name='home'),
    # url(r'^vote/', include('vote.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',login),    
    url(r'^account/login/$',login),
    url(r'^account/logout/$',logout),
    url(r'^account/regist/$',regist),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^vote/$',vote),
    url(r'^vote/poll\?id=\d+$',poll),
    url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])+'/css'}),
    url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])+'/js'}),
)
