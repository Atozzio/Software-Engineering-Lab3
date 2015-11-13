#coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bookslist/', views.bookslist, name='bookslist'),
    url(r'^detail/(?P<Book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^shanchu/(?P<book_del>[0-9]+)/$', views.shanchu, name='shanchu'),
]