# pylint: disable=E1101, E0401, E0611
import json
import requests

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt # for testing

from movies.models import Movie
from utils.scraper import MovieScraper, BayScraper

# Scraper Objects
MovieScraper = MovieScraper()
BayScraper = BayScraper()

def get_movie_details(request, imdb):
    if len(imdb) < 11:
        # Get details from OMDB
        response_dict = MovieScraper.get_by_imdb(imdb)
        return JsonResponse(status=200, data=response_dict)
    else:
        return HttpResponse(status=400)

@csrf_exempt # for testing, remove on prod
def create_movie(request):
    if request.method == 'POST':

        imdb = request.POST['imdb']

        if Movie.objects.filter(imdb_id=imdb).exists():
            return JsonResponse({ 'movie_exists': 'yes'})
        else:
            mov = Movie(
                imdb_id=imdb,
                title=request.POST['title'],
                photo=request.POST['photo'],
                year=request.POST['year'],
                rated=request.POST['rated'],
                runtime=request.POST['runtime'],
                plot=request.POST['plot'],
                release_date=request.POST['plot'])
            mov.save()
            # save object into model manager
            return JsonResponse({ 'movie_exists': 'no'})
