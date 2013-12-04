from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from users.views import *
from blog.views import *
import os.path

from django_markdown import flatpages
flatpages.register()

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vote.views.home', name='home'),
    # url(r'^vote/', include('vote.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^xadmin/',include('note.urls')),
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^markdown/',include('django_markdown.urls')),
    #account
    url(r'^$',blogs),    
    #url(r'^accounts/login/$',login),
    #url(r'^accounts/logout/$',logout),
    #url(r'^accounts/regist/$',regist),
    
    #google
    #url(r'^google',google),
    #admin
    #url(r'^admin/', include(admin.site.urls)),
    
    #vote
    url(r'^vote/',include('users.urls')),

    #blog
    url(r'^blogs/',include('blog.urls')),

    #debug
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])}),
    #url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])+'/static/css'}),
    #url(r'^charts/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])+'/static/charts'}),
    #url(r'^img/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])+'/static/img'}),
    #url(r'^tinymce/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.dirname(globals()["__file__"])+'/static/tinymce'}),
)
