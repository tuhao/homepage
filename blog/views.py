# Create your views here.
#blog.py
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from blog.models import *
from django.db.models import Count

def blogs(request,blog_page=1,sort_page=1):
    blogs = Blog.objects.order_by('pub_date')[blog_page-1:blog_page-1+20]
    sorts = Sort.objects.annotate(blog_count=Count('blog')).order_by('id')[sort_page-1:sort_page-1+20]
    return render_to_response("blog_list.html",locals(),context_instance=RequestContext(request))

def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render_to_response("blog_detail.html",locals(),context_instance=RequestContext(request))

def sort_blogs(request,sort_id,page=1):
    sorts = Sort.objects.annotate(blog_count=Count('blog')).order_by('id')[page-1:page-1+20]
    sort = get_object_or_404(Sort,pk=sort_id)
    blogs = Blog.objects.filter(sort=sort)[page-1:page-1+20]
    return render_to_response("blog_sort.html",locals(),context_instance=RequestContext(request))
