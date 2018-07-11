from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'libro', book),
    url(r'autor', author),
    url(r'^$', catalog_index)
]