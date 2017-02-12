import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self):
        self.imdb_url = 'http://www.imdb.com/title/'
        self.omdb_url = 'http://www.omdbapi.com/?'

    def get_by_omdb(self, imdb):
        pass

    def get_by_imdb(self, imdb):
        url = '{}{}'.format(self.imdb_url, imdb)
        r = requests.get(url)
        if r is not None:
            soup = BeautifulSoup(r.content, 'html.parser')
            title = soup.find("h1", { "itemprop": "name" }).get_text() # John Wick: Chapter 2 (2017)
            print(title)
        else:
            print('Error')

    def check_daily(self, imdb):
        pass

    def check_individual(self, imdb):
        pass

omdb = Scraper()
omdb.get_by_imdb('tt4425200')

# imdb_id = models.CharField(max_length=100, unique=True)
# title = models.CharField(max_length=50, unique=True)
# photo = models.CharField(max_length=250)
# year = models.CharField(max_length=4)
# rated = models.CharField(max_length=8)
# runtime = models.CharField(max_length=8)
# plot = models.CharField(max_length=250)
# release_date = models.DateField()
# dvd_date = models.DateField(blank=True, null=True)

# tracking = models.BooleanField()
# users = models.ManyToManyField(User, blank=True)
