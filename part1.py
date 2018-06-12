# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here

# Variables that contains the user credentials to access Twitter API
consumer_key = 'GPWCIGRd64c41kzZgMnYHncCJ'
consumer_secret = 'rbzLZS6ghHsp5t5nH0PfAo06eJRyKv6YcNmJ8sJJZlVbLyFVhM'
access_token = '766827375677939713-mHOg4ynoeyUYILzuyw22ULr4eTFsNgN'
access_secret = 'EfcVh4sVx9Wfmol32oTmbEk2rwoA7nBKFQPecFuBzVf0u'

# Basic listener that just prints received tweets to stdout.

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

f = open('noun_data.csv','w')

# usage should be python3 part1.py <username> <num_tweets>
print "USER: "
print "TWEETS ANALYZED: "
print "VERBS: "
print "NOUNS: "
print "ADJECTIVES: "
print "ORIGINAL TWEETS: "
print "TIMES FAVORTIED (ORIGINAL TWEETS ONLY): "
print "TIMES RETWEETED (ORIGINAL TWEETS ONLY): "
