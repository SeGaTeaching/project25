from django.contrib import admin
from .models import Author, Book, Person, Passport

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Passport)