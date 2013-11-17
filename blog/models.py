from django.db import models

# Create your models here.

class Sort(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    sort = models.ForeignKey(Sort)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    content = models.TextField(u'Blog',max_length=10000,default='',blank=True)

    #def __unicode__(self):
    #   return self.content
