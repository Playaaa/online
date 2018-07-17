from django.db import models
import datetime
# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=20,unique=True)
    pub_date = models.DateField()
    publish = models.ForeignKey(to='Publish',to_field='id',on_delete=models.CASCADE)
    author = models.ManyToManyField(to='Author')



class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=33)
    ad = models.OneToOneField(to='AuthorDetail',to_field='id',on_delete=models.CASCADE)


class Publish(models.Model):
    name = models.CharField(max_length=20)
    addr = models.CharField(max_length=20,default='不详')
    email = models.CharField(max_length=20,default='不详')


class AuthorDetail(models.Model):
    age = models.IntegerField()
    gf=models.CharField(max_length=20)