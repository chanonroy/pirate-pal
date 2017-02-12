from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^account/', include('accounts.urls')),
    url(r'^movies/', include('movies.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
