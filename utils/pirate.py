import requests
from bs4 import BeautifulSoup

pirateTop = 'https://thepiratebay.org/top/48h201'
pirateSearch = 'https://thepiratebay.org/search/'

# Quality List
quality_bad = ['CAM', 'HDCAM']
quality_okay = ['R5']
quality_good = ['DVDSCR', 'DVDRip', 'HDRip', 'Web-DL']
quality_amazing = ['BrRip']

# Validate title string and year
movie_list = ['Surfs Up 2', 'Hacksaw Ridge']


def getTop(url):
    r = requests.get(url)
    if r.raise_for_status() is None:
        soup = BeautifulSoup(r.text, 'html.parser')
        movies = soup.find_all("a", {"class": "detLink"})
        top20 = [x.get_text() for x in movies[0:19]]
    print(top20)

    # Does fuzzy wuzzy string matching - should 100% match


def checkIndividual(url):
    # should go lower case
    pass

getTop(pirateTop)
