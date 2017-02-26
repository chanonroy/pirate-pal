from movies.models import Movie
from utils.scraper import MovieScraper, BayScraper

from celery.task import PeriodicTask
from datetime import timedelta

class ProcessClicksTask(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(self, **kwargs):
        print('This is working')
