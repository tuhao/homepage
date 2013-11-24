# Create your views here.
# blog.py
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import *
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import randrange


def paginate_sorts(request):
    sort_list = Sort.objects.annotate(
        blog_count=Count('blog')).all()
    paginator = Paginator(sort_list, 5)
    sort_page = request.GET.get('sort_page')
    try:
        sorts = paginator.page(sort_page)
    except PageNotAnInteger:
        sorts = paginator.page(1)
    except EmptyPage:
        sorts = paginator.page(paginator.num_pages)
    return sorts


def blog_tags():
    total = Blog.objects.all().count()
    try:
        start = randrange(0, int(total) - 20)
    except ValueError:
        start = 0
    blogs = Blog.objects.order_by('pub_date')[start:start + 20]
    tagclouds = set()
    for b in blogs:
        tag_list = b.tags.split(' ')
        for tag in tag_list:
            tagclouds.add(tag)
    return tagclouds


def friend_links():
    links = Link.objects.all()
    return links


def blogs(request):
    sorts = paginate_sorts(request)
    blogs = Blog.objects.order_by('pub_date')[0:10]
    tagclouds = blog_tags()
    links = friend_links()
    return render_to_response("blog_list.html", locals(), context_instance=RequestContext(request))


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    tags = blog.tags.split(' ')
    tagclouds = blog_tags()
    links = friend_links()
    blogs = Blog.objects.order_by('pub_date')
    sorts = paginate_sorts(request)
    return render_to_response("blog_detail.html", locals(), context_instance=RequestContext(request))


def sort_blogs(request, sort_id):
    sort = get_object_or_404(Sort, pk=sort_id)
    sort_blogs = Blog.objects.filter(sort=sort)
    sorts = paginate_sorts(request)
    blogs = Blog.objects.order_by('pub_date')
    tagclouds = blog_tags()
    links = friend_links()
    return render_to_response("blog_sort.html", locals(), context_instance=RequestContext(request))


def blog_search(request):
    query = request.GET.get('q', None)
    if query:
        try:
            r = Blog.search.query(query)
            results = list(r)
        except Exception, e:
            results = list()
        context = {'results': results, 'query':
                   query, 'search_meta': r._sphinx}
    else:
        results = list()
        context = {'results': results}
    return render_to_response('blog_search.html', context, context_instance=RequestContext(request))


def about(request):
    abouts = About.objects.all()
    return render_to_response("about_me.html", locals(), context_instance=RequestContext(request))
