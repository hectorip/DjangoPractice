from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'libro/(?P<id>[0-9]+)', book),
    url(r'autor$', author),
    url(r'pais/(?P<id>[0-9]+)$', country_detail, name='country_detail'),
    url(r'autor/(?P<id>[0-9]+)', author_detail),
    url(r'^$', catalog_index)
]
