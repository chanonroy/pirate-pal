from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='movies.dashboard'),
    url(r'^watchlist/', views.index, name='movies.watchlist'),
    url(r'^add/', views.index, name='movies.add'),

]
