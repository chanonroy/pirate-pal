from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'movies/dashboard.html', context=None)

@login_required
def add(request):
    return render(request, 'movies/add_movie.html', context=None)

# URL to run API proxy to scrape/request IMDB movie
