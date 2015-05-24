from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time

consumer_key = "e5y3bEkSNqv571ZJdnosGragb" 
consumer_secret = "vPIBsIOn2wlzpxoPAyEKSibovbNVGUYtw83E56gE3TA4nQg8I1"

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)

api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,q='Obama',since='2015-05-20',until='2015-05-21').items(10):
    print tweet.text
