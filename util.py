from pyshorteners.shorteners import Shortener
from random import choice

# list of shortners
#1) GoogleShortener
#2) TinyurlShortener
#3) IsgdShortener
#4) SentalaShortener

shorts = ['GoogleShortener', 'TinyurlShortener', 'IsgdShortener', 'SentalaShortener']


def short(url):
    shurl = Shortener(choice(shorts))
    return shurl.short(url)

