from django.contrib import admin
from django.urls import path,include
from .views import movie, book, technology, blog


urlpatterns = [
    path("movie",movie),
    path("book",book),
    path("technology",technology),
    path("blog",blog)
]
