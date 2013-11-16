from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class User(models.Model):
#    username = models.CharField(max_length=10)
#    email = models.EmailField()
#    password = models.CharField(max_length=10)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question

class Choise(models.Model):
    poll = models.ForeignKey(Poll)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choise_text

class Record(models.Model):
    poll = models.ForeignKey(Poll)
    user = models.ForeignKey(User)
    choise = models.ForeignKey(Choise)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(u'Blog',max_length=10000,default='',blank=True)

