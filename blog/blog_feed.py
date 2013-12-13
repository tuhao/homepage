from django.contrib.syndication.views import Feed
from blog.models import Blog
from django.core.urlresolvers import reverse
from django.conf import settings
import re

HOSTNAME = getattr(settings,"HOSTNAME",None)

class LastestBlog(Feed):
	title = "Lastest blogs"
	link = "http://" + HOSTNAME
	description = "Rss"

	def items(self):
		return Blog.objects.order_by('-id')[:10]

	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return self.striptags(item.content)[:150] + "..."

	def item_link(self,item):
		return self.link + reverse("blog.views.blog_detail",args=(item.id,))

	def striptags(self,content):
		pattern = re.compile(r'</?[^>]*>|\&nbsp;?|\s+')
		return pattern.sub("", content)

