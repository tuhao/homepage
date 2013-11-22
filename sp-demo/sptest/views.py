from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
from models import Story
from django.shortcuts import render_to_response


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query', None)
        r = Story.search.query(query)
        story = list(r)
        context = {'story': story, 'query': query, 'search_meta': r._sphinx}
    else:
        story = list()
        context = {'story': story}
    return render_to_response('search.html', context)
