# Create your views here.
# blog.py
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import *
from django.db.models import Count

PAGE_SIZE = 10


def start_index(page):
    if page <= 0:
        return 0
    return (int(page) - 1) * PAGE_SIZE


def end_index(page):
    return int(page) * PAGE_SIZE


def max_page(total_size):
    total = int(total_size)
    if total % PAGE_SIZE == 0:
        return total / PAGE_SIZE
    else:
        return (total - (total % PAGE_SIZE)) / PAGE_SIZE + 1


def validate(page, total):
    if int(page) > max_page(total):
        return max_page(total)
    if int(page) < 1:
        return 1
    return page


def sortp(sort_page):
    sort_total = Sort.objects.count()
    sp = validate(sort_page, sort_total)
    return start_index(sp), end_index(sp)


def blogp(blog_page):
    blog_total = Blog.objects.count()
    bp = validate(blog_page, blog_total)
    return start_index(bp), end_index(bp)


def blogs(request, sort_page=1, blog_page=1):
    sp = sortp(sort_page)
    bp = blogp(blog_page)
    blogs = Blog.objects.order_by('pub_date')[
        bp[0]:bp[1]]
    sorts = Sort.objects.annotate(
        blog_count=Count('blog')).order_by('id')[sp[0]:sp[1]]
    blog_total = Blog.objects.count()
    return render_to_response("blog_list.html", locals(), context_instance=RequestContext(request))


def blog_detail(request, blog_id, sort_id, blog_page=1, sort_page=1):
    sp = sortp(sort_page)
    bp = blogp(blog_page)
    sorts = Sort.objects.annotate(
        blog_count=Count('blog')).order_by('id')[sp[0]:sp[1]]
    sort = get_object_or_404(Sort, pk=sort_id)
    blogs = Blog.objects.filter(sort=sort)[bp[0]:bp[1]]
    blog = get_object_or_404(Blog, pk=blog_id)
    blog_total = Blog.objects.count()
    return render_to_response("blog_detail.html", locals(), context_instance=RequestContext(request))


def sort_blogs(request, sort_id, blog_page=1, sort_page=1):
    sp = sortp(sort_page)
    bp = blogp(blog_page)
    sorts = Sort.objects.annotate(
        blog_count=Count('blog')).order_by('id')[sp[0]:sp[1]]
    sort = get_object_or_404(Sort, pk=sort_id)
    blogs = Blog.objects.filter(sort=sort)[bp[0]:bp[1]]
    blog_total = Blog.objects.count()
    return render_to_response("blog_sort.html", locals(), context_instance=RequestContext(request))
