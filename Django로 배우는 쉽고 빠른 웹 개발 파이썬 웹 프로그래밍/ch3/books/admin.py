from django.contrib import admin

# Register your models here.

from django.contrib import admin
from books.models import Book, Author, Publisher

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)