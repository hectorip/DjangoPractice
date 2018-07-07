from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# daniel nos va explicar que tiene Request
def catalog_index(request):
    """
    Vista basada en función
    """
    return HttpResponse("Holi")

def book(request):
    return render(request, 'catalog/index.html')
