from django import forms
from django_markdown.widgets import MarkdownWidget
from blog.models import Sort,Blog

class MarkdownForm(forms.Form):
    sort_id = forms.CharField()
    blog_title = forms.CharField()
    blog_content = forms.CharField(widget=MarkdownWidget())
    blog_tags = forms.CharField()


    def clean_sort_id(self):
        sort_id = self.cleaned_data['sort_id']
        if sort_id == "0":
        	raise forms.ValidationError("Sort must be chosed")
        try:
        	exist_sort = Sort.objects.get(id=int(sort_id))
        except Sort.DoesNotExist:
        	raise forms.ValidationError("sort does not exits")
        return sort_id

    def clean_blog_title(self):
 	    blog_title = self.cleaned_data['blog_title']
 	    if len(blog_title) > 100:
 			raise forms.ValidationError("title's length must lt 100 characters")
 	    try:
 			exist_blog = Blog.objects.get(title=blog_title)
 	    except Exception, e:
 			pass
 	    else:
 			raise forms.ValidationError("Blog title exists.")
 	    return blog_title

    def clean_blog_content(self):
        blog_content = self.cleaned_data['blog_content']
        content_length = len(blog_content.strip())
        if content_length == 0 or content_length > 10000:
            raise forms.ValidationError("content length 1-10000")
        return blog_content


    def clean_blog_tags(self):
    		blog_tags = self.cleaned_data['blog_tags']
    		if len(blog_tags.strip()) == 0:
    			raise forms.ValidationError("tags should not be empty")
    		return blog_tags 