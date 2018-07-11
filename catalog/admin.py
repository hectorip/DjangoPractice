from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country