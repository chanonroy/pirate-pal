from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movie/get/(?P<imdb>\w+)', views.get_movie_details, name='api.get_movie'),
    url(r'^movie/create/', views.create_movie, name='api.create_movie'),
]
