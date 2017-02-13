from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'quality', 'tracking', 'imdb_id', 'release_date')
    list_filter = ('quality', 'tracking', 'release_date')
    search_fields = ['title', 'imdb_id']
