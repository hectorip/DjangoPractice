from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Book, Author, Country
# Create your views here.

# daniel nos va explicar que tiene Request
def catalog_index(request):
    """
    Vista basada en función
    """
    books = Book.objects.all()

    return render(
        request,
        'catalog/index.html',
        context={"books": books}
    )


def book(request, id):
    book = get_object_or_404(Book, pk=id)

    context = {
        "book": book
    }
    return render(
        request,
        'catalog/book.html',
        context=context)


def author(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(
        request,
        'catalog/author.html',
        context=context
    )

def author_detail(request, id):
    # author = Author.objects.get(pk=id)
    author = get_object_or_404(Author, pk=id)
    context = {
        "author": author
    }
    return render(
        request,
        'catalog/author_detail.html',
        context=context
    )

def country_detail(request, id):
    country = get_object_or_404(Country, pk=id)
    context = {
        "country": country
    }

    return render(
        request,
        'catalog/country_detail.html',
        context=context
    )