#coding:utf-8
from django.db import models

class Author(models.Model):
    AuthorID = models.IntegerField(default = 0)
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField(default = 0)
    Country = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.Name
    
class Book(models.Model):
    ISBN = models.CharField(max_length = 13)
    Title = models.CharField(max_length = 40)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 50)
    PublishDate = models.DateField('date published')
    Price = models.FloatField()
    def __unicode__(self):
        return self.Title
    