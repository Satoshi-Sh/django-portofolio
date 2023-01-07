from django.db import models

# Create your models here.


class Project(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image= models.URLField(max_length=250)
    github = models.URLField(max_length=250,default='')
    page = models.URLField(max_length=250,default='')
    def short(self):
        return self.description[0:50] +'...'
    def technologyList(self):
        return self.split(',')
    def __str__(self):
        return self.title