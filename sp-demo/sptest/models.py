# coding:utf-8
from django.db import models
from djangosphinx.models import SphinxSearch


class Story(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.CharField(max_length=200)

    search = SphinxSearch(index='sptest_story')

    def __unicode__(self):
    	return self.title
