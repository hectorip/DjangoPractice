from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'libro', book),
    url(r'$', catalog_index)
]