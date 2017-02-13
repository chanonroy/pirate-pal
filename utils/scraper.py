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

        bay_list = ['Hacksaw Ridge (2016) DVDSCR 650MB - MkvCage', 'Doctor.Strange.2016.1080P.XVID.AC3.HQ.Hive-CM8' ]
        db_list = ['Hacksaw Ridge 2016', 'Doctor Strange 2016', 'Hugo 2012']
        results_dict = {}

        for bay_item in bay_list:
            for db_movie in db_list:
                self.validate_movies(bay_item, db_movie, results_dict)

        return results_dict

    def validate_movies(self, bay_item, db_movie, results_dict):
        """
        1. Check if movie/string from db match a bay_item (tokenized subset ratio)
        2. If match, check for quality and add to results dictionary
        """

        value = fuzz.token_set_ratio(db_movie, bay_item)
        if value == 100:
            quality_rating = self.validate_quality(bay_item)
            results_dict[db_movie] = quality_rating

    def validate_quality(self, bay_item):
        """ Returns a STR of quality (key in dict) if values match PirateBay string (bay_item) """

        for rating, words in self.quality.items():
            for word in words:
                if word.lower() in bay_item.lower():
                    return rating

    def check_top(self, imdb):
        """ Check the top new hits from the Bay (Daily) """
        pass

    def check_solo(self, imdb):
        """ Check an individual film on the Bay (Weekly) """
        pass

    def check_if_dvd(self, imdb):
        """ Check if a film has been released on dvd (Monthly) """
        pass

movie = MovieScraper()
bay = BayScraper()

quality = bay.speak()
print(quality)
