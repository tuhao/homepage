# Create your views here.
# blog.py
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import *
from django.db.models import Count

pagenum = 10


def start_index(page):
    if page <= 0:
        return 0
    return (int(page) - 1) * pagenum


def end_index(page):
    return int(page) * pagenum


def blogs(request, sort_page=1, blog_page=1):
    try:
        blogs = Blog.objects.order_by('pub_date')[
            start_index(blog_page):end_index(blog_page)]
        sorts = Sort.objects.annotate(blog_count=Count('blog')).order_by(
            'id')[start_index(sort_page):end_index(sort_page)]
    except Exception, e:
        sorts = Sort.objects.annotate(blog_count=Count('blog')).order_by(
            'id')[0:pagenum]
        blogs = Blog.objects.order_by('pub_date')[0:pagenum]
    blog_total = Blog.objects.count()
    return render_to_response("blog_list.html", locals(), context_instance=RequestContext(request))


def blog_detail(request, blog_id, sort_id,blog_page=1,sort_page=1):
    sorts = Sort.objects.annotate(
        blog_count=Count('blog')).order_by('id')[start_index(sort_page):end_index(sort_page)]
    sort = get_object_or_404(Sort, pk=sort_id)
    blogs = Blog.objects.filter(sort=sort)[
        start_index(blog_page):end_index(blog_page)]
    blog_total = Blog.objects.count()
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_to_response("blog_detail.html", locals(), context_instance=RequestContext(request))


def sort_blogs(request, sort_id, blog_page=1, sort_page=1):
    sorts = Sort.objects.annotate(
        blog_count=Count('blog')).order_by('id')[start_index(sort_page):end_index(sort_page)]
    sort = get_object_or_404(Sort, pk=sort_id)
    blogs = Blog.objects.filter(sort=sort)[
        start_index(blog_page):end_index(blog_page)]
    blog_total = Blog.objects.count()
    return render_to_response("blog_sort.html", locals(), context_instance=RequestContext(request))
