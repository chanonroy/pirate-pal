from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    imdb_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=50, unique=True)
    photo = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=8)
    runtime = models.CharField(max_length=8)
    plot = models.CharField(max_length=250)
    release_date = models.DateField()
    dvd_date = models.DateField(blank=True, null=True)

    tracking = models.BooleanField()
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.year)
