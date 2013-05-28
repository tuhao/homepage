from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choise(models.Model):
    poll = models.ForeignKey(Poll)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


