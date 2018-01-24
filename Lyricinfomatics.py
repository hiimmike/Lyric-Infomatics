import pprint 
from collections import Counter 
import re


filename = 'C:\\Users\\MikeB\\Documents\\PYTHON\\song01.txt'
filename2 = 'C:\\Users\\MikeB\\Documents\\PYTHON\\song02.txt'

theInside = open(filename, 'r')
theInside = theInside.read().lower()


def testing():
        with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                        searchObj = re.search( r'genre:rock', line, re.I)
                        if searchObj:         
                                indi = Counter(theInside.split()) 
                                top = indi.most_common(5) 
                                pprint.pprint(top)


testing()
                                
# To-Do List:
# Ignore the tags
# Genre
# Year
# Total number of words
# Number of unique words
# Frequency of indiv. words
# Most common words
# Frequency of Indiv. letters
# Unique words to total words
# Frequency of word pairs
