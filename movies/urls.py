from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='movies.dashboard'),
    url(r'^watchlist/', views.index, name='movies.watchlist'),
    url(r'^add/', views.add, name='movies.add'),
    url(r'^archive/', views.archive, name='movies.archive'),

]
