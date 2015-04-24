from django.db import models
import datetime


'''Main in Blog and User's query and Comment query, insert. '''
class Blog(models.Model):
    title = models.CharField(max_length=30)
    summery = models.CharField(max_length=200)
    content = models.TextField()
    create_time = models.DateTimeField()

    def __unicode__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=30)
    #create_time = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    content = models.TextField()
    create_time = models.DateTimeField()

    def __unicode__(self):
        return u'%s-%s' % (self.user, self.blog)
