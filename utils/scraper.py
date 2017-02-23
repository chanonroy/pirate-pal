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
        url = '{}{}'.format(self.omdb_url, 'i=' + imdb)
        r = requests.get(url)
        if r is not None:
            return r.json()
        else:
            print('OMDB API is down')

    def get_by_imdb(self, imdb):
        """ Use IMDB to get details """
        url = '{}{}'.format(self.imdb_url, imdb)
        r = requests.get(url)
        if r is not None:
            soup = BeautifulSoup(r.content, 'html.parser')
            imdb_id = imdb
            title = soup.find("h1", { "itemprop": "name" }).get_text() # John Wick: Chapter 2 (2017)
            photo = soup.find("div", { "class": "poster" }).find("img")['src'].strip()
            year = soup.find("span", { "id": "titleYear"}).find("a").get_text().strip()
            rated = soup.find("meta", { "itemprop": "contentRating"})['content'].strip()
            runtime = soup.find("time", { "itemprop": "duration"}).get_text().strip()
            plot = soup.find("div", { "class": "summary_text"}).get_text().strip()
            release_date = soup.find("a", { "title": "See more release dates"}).get_text().strip()

            # tracking = false
            # users = set to request.user
        else:
            print('Error')

class BayScraper:
    """ Scrape the Bay to check for quality """

    def __init__(self):
        self.db_list = []
        self.top_url = 'https://thepiratebay.org/top/48h201'
        self.search_url = 'https://thepiratebay.org/search/'
        self.quality = collections.OrderedDict()
        self.quality['Great'] = ['1080p', 'BrRip', 'BluRay']
        self.quality['Good'] = ['720p', 'HDRip', 'Web-DL']
        self.quality['Okay'] = ['R5', 'DVDSCR', 'DVDRip']
        self.quality['Poor'] = ['CAM', 'HDCAM', 'HDTS', 'HD-TS', 'TS']

    def update_db_list(self):
        """ Makes sure db_list is up to date with movies.tracking = True (Django queryset) """

        self.db_list = ['Hacksaw Ridge 2016', 'Doctor Strange 2016', 'Hugo 2012', 'Man Down 2016']

    def get_bay_list(self, url):
        """ Return list of raw pirate bay strings """
        r = requests.get(url)
        if r is not None:
            soup = BeautifulSoup(r.content, 'html.parser')
            titles = soup.find_all("div", class_= "detName")[0:10]
            results = [title.get_text() for title in titles]
            return results
        else:
            print('get_bay_list error. !200')

    def check_top(self):
        """ Returns dict with key[title] and value[quality] if present in top list """

        results_dict = {}
        bay_list = self.get_bay_list(self.top_url)
        db_list = self.db_list

        for bay_item in bay_list:
            for db_movie in db_list:
                self.validate_movies(bay_item, db_movie, results_dict)

        return results_dict

    def check_solo(self, name):
        """ From movie name, returns value of quality as a STR """

        bay_list = self.get_bay_list(self.search_url + name)
        print(bay_list)
        return self.validate_quality(bay_list[0])

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
