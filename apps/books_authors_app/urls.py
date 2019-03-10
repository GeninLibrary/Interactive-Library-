
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^attribute', views.attribute),
    url(r'^author$', views.createAuthor),
    url(r'^author/add$', views.addAuthor),
    url(r'^author/show/(?P<id>\d+)$', views.showAuthor),
    url(r'^delete/author/(?P<id>\d+)$', views.deleteAuthor),
    url(r'^book$', views.createBook),
    url(r'^book/add$', views.addBook),
]
