""" Test for fuzzywuzzy """
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

test1 = 'The Edge of Seventeen 2016'
test2 = 'Nocturnal Animals 2 2016'

# year

real1 = 'The Edge of Seventeen (2016) DVDSCR 650MB - MkvCage'
real2 = 'Nocturnal.Animals.2.2016.DVDScr.XVID.AC3.HQ.Hive-CM8'

output = fuzz.token_set_ratio(test2, real2)

print(output)
