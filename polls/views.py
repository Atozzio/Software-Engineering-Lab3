#from django.shortcuts import render_to_response
#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Author, Book
from django.template import RequestContext, loader


def index(request):
    Author_list = Author.objects.order_by('AuthorID')
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, { 
        'Author_list': Author_list,
    })
    return HttpResponse(template.render(context))
    
def bookslist(request):
    Book_list = Book.objects.order_by('Title')
    template = loader.get_template('polls/bookslist.html')
    context = RequestContext(request, { 
        'Book_list': Book_list,
    })
    return HttpResponse(template.render(context))

def detail(request, Book_id):
    book = get_object_or_404(Book, pk=Book_id)
    author = book.AuthorID
    return render(request, 'polls/detail.html', locals())
       
def shanchu(request, book_del):
    b = Book.objects.get(id=book_del)
    b.delete()
    return render(request, 'polls/shanchu.html')
#def add(request):
    
