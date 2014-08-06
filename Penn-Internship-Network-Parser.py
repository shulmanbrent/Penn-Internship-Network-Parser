from __future__ import division
import nltk, re, pprint
from urllib import urlopen
from nltk.corpus import PlaintextCorpusReader, stopwords
from HTMLParser import HTMLParser
from nltk.tokenize import *
from bs4 import BeautifulSoup
import os
#from nltk.book import *

from nltk.tokenize.punkt import PunktWordTokenizer
import csv

corpus_root = "C:\Users\Brent\Documents\My Research\Penn-Internship-Network-Parser"
def getCorpusFiles():
    #file names for all the documents in the corpus of transcripts
    corpus_root = "C:\Users\Brent\Documents\My Research\Penn-Internship-Network-Parser"
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    fileIds = wordlists.fileids()
    return fileIds
    
x = getCorpusFiles()
file = x[-2]
file = open(os.path.join(corpus_root, file), 'r')
soup = BeautifulSoup(file)
print soup.findAll('p', recursive = False)