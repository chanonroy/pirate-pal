from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^account/', include('accounts.urls')),
    url(r'^my-movies/', include('movies.urls')),
    url(r'^admin/', admin.site.urls),
]
