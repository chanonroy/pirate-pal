# pylint: disable=E1101, E0401, E0611, C0111
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Movie

@login_required
def index(request):

    movies = Movie.objects.filter(users=request.user).filter(tracking=True) # .order_by('param')
    context_dict = {'movies': movies}

    return render(request, 'movies/dashboard.html', context=context_dict)

@login_required
def archive(request):

    movies = Movie.objects.filter(users=request.user).filter(tracking=False)
    context_dict = {'movies': movies}

    return render(request, 'movies/archive.html', context=context_dict)

@login_required
def add(request):
    return render(request, 'movies/add_movie.html', context=None)

# URL to run API proxy to scrape/request IMDB movie
# POST send IMDB id --> get or create movie, assign user m2m to that movie.
