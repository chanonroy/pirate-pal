import collections
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class MovieScraper:
    """ Get movie details from IMDB id """

    def __init__(self):
        self.imdb_url = 'http://www.imdb.com/title/'
        self.omdb_url = 'http://www.omdbapi.com/?'

    def get_by_omdb(self, imdb):
        """ Use OMDB to get details """
        pass

    def get_by_imdb(self, imdb):
        """ Use IMDB to get details """
        url = '{}{}'.format(self.imdb_url, imdb)
        r = requests.get(url)
        if r is not None:
            soup = BeautifulSoup(r.content, 'html.parser')
            # imdb_id
            title = soup.find("h1", { "itemprop": "name" }).get_text() # John Wick: Chapter 2 (2017)
            # photo
            # year
            # rated
            # runtime
            # plot
            # release_date

            # tracking = false
            # users = set to request.user
            print(title)
        else:
            print('Error')

class BayScraper:
    """ Scrape the Bay to check for quality """

    def __init__(self):
        self.top_url = 'https://thepiratebay.org/top/48h201'
        self.search_url = 'https://thepiratebay.org/search/'
        self.quality = collections.OrderedDict()
        self.quality['Great'] = ['1080p', 'BrRip', 'BluRay']
        self.quality['Good'] = ['720p', 'DVDSCR', 'DVDRip', 'HDRip', 'Web-DL']
        self.quality['Okay'] = ['R5']
        self.quality['Poor'] = ['CAM', 'HDCAM']

    def speak(self):

        bay_list = ['Hacksaw Ridge (2016) DVDSCR 650MB - MkvCage', 'Doctor.Strange.2016.DVDScr.XVID.AC3.HQ.Hive-CM8' ]
        db_list = ['Hacksaw Ridge 2016', 'Doctor Strange 2016']

        # Check Title
        for bay_item in bay_list:
            for db_movie in db_list:
                # fuzzy similarity ratio
                value = fuzz.token_set_ratio(db_movie, bay_item)
                if value == 100:

                    # Check Quality
                    for key, value in self.quality.items():
                        # check if the torrent title matches a value then return key
                        for item in value:
                            if item in bay_item:
                                return "{} - Quality: {}".format(db_movie, key)

    def validate_quality(self):
        pass

    def check_top(self, imdb):
        """ Check the top new hits from the Bay (Daily) """
        pass

    def check_solo(self, imdb):
        """ Check an individual film on the Bay (Weekly) """
        pass

movie = MovieScraper()
bay = BayScraper()

quality = bay.speak()
print(quality)
