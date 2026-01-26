# movies/admin.py
from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',) # add comma to let python know it's a tuple and not string
    list_display = ('title', 'number_in_stock', 'daily_rate')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
