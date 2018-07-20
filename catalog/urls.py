from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'libro/(?P<id>[0-9]+)', book, name='book_detail'),
    url(r'libro/registrar', register_book, name='book_registration'),
    url(r'autores$', author_index, name='home'),
    url(r'autor/(?P<id>[0-9]+)', author_detail, name='author_detail'),
    url(r'pais/(?P<id>[0-9]+)$', country_detail, name='country_detail'),
    url(r'^$', catalog_index, name='catalog_index')
]
