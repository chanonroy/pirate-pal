from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='accounts.login'),
    url(r'^register/$', views.RegisterView.as_view(), name='accounts.register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='accounts.logout'),
]
