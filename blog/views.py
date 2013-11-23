# Create your views here.
# blog.py
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import *
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate_sorts(request):
    sort_list = Sort.objects.annotate(
        blog_count=Count('blog')).all()
    paginator = Paginator(sort_list,5)
    sort_page = request.GET.get('sort_page')
    try:
        sorts = paginator.page(sort_page)
    except PageNotAnInteger:
        sorts = paginator.page(1)
    except EmptyPage:
        sorts = paginator.page(paginator.num_pages)
    return sorts

def blogs(request):
    sorts = paginate_sorts(request)
    blogs = Blog.objects.order_by('pub_date')[0:10]
    return render_to_response("blog_list.html", locals(), context_instance=RequestContext(request))


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.order_by('pub_date')
    sorts = paginate_sorts(request)
    return render_to_response("blog_detail.html", locals(), context_instance=RequestContext(request))


def sort_blogs(request, sort_id):
    sort = get_object_or_404(Sort, pk=sort_id)
    sort_blogs = Blog.objects.filter(sort=sort)
    sorts = paginate_sorts(request)
    blogs = Blog.objects.order_by('pub_date')
    return render_to_response("blog_sort.html", locals(), context_instance=RequestContext(request))


def blog_search(request):
    query = request.GET.get('q', None)
    r = Blog.search.query(query)
    blog = list(r)
    context = {'blog': blog, 'query': query, 'search_meta': r._sphinx}
    return render_to_response('blog_search.html', locals(), context_instance=RequestContext(request))


def search_test(request):
    if request.method == 'POST':
        query = request.POST.get('query', None)
        r = Blog.search.query(query)
        blog = list(r)
        context = {'blog': blog, 'query': query, 'search_meta': r._sphinx}
    else:
        blog = list()
        context = {'blog': blog}
    return render_to_response('search.html', locals(), context_instance=RequestContext(request))
