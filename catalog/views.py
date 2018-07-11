from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import Book, Author
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
    try:
        book = Book.objects.get(pk=id)
    except Exception:
        return render(request, '404.html', status=404)

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
