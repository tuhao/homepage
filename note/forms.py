from django import froms
from django_markdown.widgets import MarkdownWidget
from blog.models import Sort,Blog

class MarkdownForm(forms.Form):
    sort = form.CharField()
    title = form.CharField()
    content = forms.TextField( widget=MarkdownWidget() )
    tags = form.CharField()

    def clean_sort(self):
        sort = self.cleaned_data['sort.id']
        if sort == "0":
        	raise forms.ValidationError("sort must be chosed")
        try:
        	exist_sort = Sort.objects.get(id=int(sort))
        except Sort.DoesNotExist:
        	raise forms.ValidationError("sort does not exits")
        return exist_sort

    def clean_title(self):
 	    title = self.cleaned_data['blog.title']
 	    if len(title) > 100:
 			raise forms.ValidationError("title's length must lt 100 characters")
 	    try:
 			exist_blog = Blog.objects.get(title=title)
 	    except Exception, e:
 			pass
 	    else:
 			raise forms.ValidationError("Blog title exists.")
 	    return title

    def clean_tags(self):
    		tags = self.cleaned_data['blog.tags']
    		if len(tags.strip()) == 0:
    			raise forms.ValidationError("tags should not be empty")
    		return tags 