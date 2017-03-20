# pylint: disable=E1101, E0401, E0611, C0111
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    imdb_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=50, unique=True)
    photo = models.CharField(max_length=250)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=8)
    runtime = models.CharField(max_length=8)
    plot = models.CharField(max_length=250)
    release_date = models.DateField()

    QUALITY_RATING = (
        ('A', 'Best (1080p)'),
        ('B', 'Good (720p)'),
        ('C', 'Okay (DVDRip)'),
        ('D', 'Poor (CAM)'),
    )

    quality = models.CharField(max_length=1, choices=QUALITY_RATING, blank=True)
    tracking = models.BooleanField()
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return "{} {}".format(self.title, self.year)
