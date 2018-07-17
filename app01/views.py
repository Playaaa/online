from django.shortcuts import render,HttpResponse
from app01.models import Book,Author,Publish,AuthorDetail
# Create your views here.




def head(request):
    pass





def add(request):
    Book.objects.create(title='葵花宝典',pub_date=2012-12-12)




