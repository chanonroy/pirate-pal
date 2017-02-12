from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse

import requests
import json

API_URL = getattr(settings, 'MOVIE_API')

def get_movie_details(request):
    pass
