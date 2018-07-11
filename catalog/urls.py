from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'libro/(?P<id>[0-9]+)', book),
    url(r'autor', author),
    url(r'^$', catalog_index)
]
