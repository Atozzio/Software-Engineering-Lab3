# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render_to_response
#import MySQLdb
#from django.template import loader
from polls.models import Author, Book

    
def hello(request):
    return render_to_response('hello.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']   
        author = Author.objects.filter(Name__icontains=q)
        book = Book.objects.filter(AuthorID__Name=q)
        return render_to_response('result.html',
                                  {'author': author, 'query': q, 'book': book})
    else:
        return render_to_response('hello.html', {'error': True})