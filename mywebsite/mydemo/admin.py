from django.contrib import admin
from .models import Movie, Book, Technology, Blog


class MovieAdmin(admin.ModelAdmin):
    list_display = ['moviename', 'moviescore', 'viewingtime', 'remarks'] 

class BookAdmin(admin.ModelAdmin):
    list_display = ['bookname', 'bookscore', 'booktimestart', 'booktimeend', 'remarks']

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['technologyname', 'technologyscore'] 

class BlogAdmin(admin.ModelAdmin):
    list_display = ['blogtype', 'blogtime', 'remarks']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Blog, BlogAdmin)
