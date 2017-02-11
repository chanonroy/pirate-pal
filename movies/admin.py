from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tracking', 'imdb_id', 'release_date', 'dvd_date')
    list_filter = ('tracking', 'release_date', 'dvd_date')
    search_fields = ['title']
