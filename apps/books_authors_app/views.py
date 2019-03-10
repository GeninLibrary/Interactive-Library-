# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect

################################# Routes from index #########################################################

def index(request):
    try:
        context = {
            "authors": Author.objects.all(),
            "books": Book.objects.all(),
        }
        return render(request, 'books_authors_app/index.html', context)
    except:
        return render(request, 'books_authors_app/index.html')

def attribute(request):
    Author.objects.get(id = request.POST['author']).books.add(Book.objects.get(id = request.POST['book']).id)
    return redirect ('/')

##Authors##

def createAuthor(request):
    return render(request, 'books_authors_app/author.html')

def showAuthor(request, id):
    context = {
        "author": Author.objects.get(id = id),
        "books": Author.objects.get(id=id).books.all()
    }
    return render(request, 'books_authors_app/page.html', context)

def deleteAuthor(request, id):
    Author.objects.get(id = id).delete()
    return redirect ('/')

##Books

def createBook(request):
    return render(request, 'books_authors_app/book.html')

#################################### Routes stemming from add author pge ####################################

def addAuthor(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    context = {
        "authors": Author.objects.all(),
    }
    return redirect('/')

#################################### Routes stemming from add book pge ####################################


def addBook(request):
    print request.POST
    Book.objects.create(name=request.POST['name'], info=request.POST['info'])
    context = {
        "books": Book.objects.all(),
    }
    return redirect('/')
