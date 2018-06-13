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

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

public_tweets = api.home_timeline() # One possible method! Check out: http://tweepy.readthedocs.io/en/v3.5.0/api.html#timeline-methods
print(type(public_tweets)," is the type of public tweets")

for tweet in public_tweets:
    print("\n*** type of the tweet object that is included ***\n")
    print(type(tweet),"type of one tweet")
    print(tweet) ## Huh. That's not easy to read.

# Let's pull apart one tweet to take a look at it.
single_tweet = public_tweets[0]

## What are the tags?
print("\n*** tags of the tweet dictionary ***")
print(single_tweet.keys())

## Well, some of these look interesting.
## For example,
print("\nHere's the text of the tweet:")
print(single_tweet["text"])
print("\n")
print("Here are the # of favorites of that tweet:")
print(single_tweet["favorite_count"])

## Taking a look at the keys, try printing some other attributes of the tweet!

## But what if I don't want just my own public timeline's tweets -- I want to search for a certain phrase on Twitter!
print("********\n\n\n*******")
results = api.search(q="NBA")
print(type(results), "is the type of the results variable")

## OK, it's a dictionary. What are its keys?
print(results.keys())

## That 'statuses' key looks interesting.
print(type(results["statuses"]), "is the type of results['statuses']")
## OK, that's a list! Hmm. What's the type of the first element in it?
print(type(results["statuses"][0]), "is the type of the first element in the results")
## OK, that's a dictionary. What are its keys? I have a suspicion they'll be the same as the Tweet dictionary I saw before...
## I'm gonna assign that one tweet to a variable to make it easier.
nba_tweet = results["statuses"][0]
## Now, what are its keys?
print("\nThe keys of the tweet dictionary:")
print(nba_tweet.keys())

## And the list of tweets is in results["statuses"]..
list_of_nba_tweets = results["statuses"]

## Iterate over the tweets you get back...
## And print the text of each one!
for tweet in list_of_nba_tweets:
    print(tweet["text"])
    print("\n")

## Note that there are a bunch of options in the search you can try -- to get more tweets, etc. But for now, look at how much you can access with the basics.

## Here's code to update a status -- uncomment below lines if you fill them in to post something to Twitter
# stat_text = "" # A string for what you want to be posted on your twitter account
# ## Uncomment the following line to post a new status
# api.update_status(stat_text)

api = tweepy.API(auth)

f = open('noun_data.csv','w')
# Write some explainations and headers for people to read and understand the file
w_str0 = "We got five most frequent nouns by searching the word using Twitter API. \nHere are the results after sorting the nouns by their number of appearance - most to least: \n"
f.write(w_str0 + '\n')
f.write("  \n\n")
w_str1 = "Noun, Number"
f.write(w_str1 + '\n')

for noun in sorted_noun_lst:
	w_str  = "{}, {}".format(lst.noun, lst.number)
	f.write(w_str  + '\n')

f.close()

# usage should be python3 part1.py <username> <num_tweets>
print "USER: "
print "TWEETS ANALYZED: "
print "VERBS: "
print "NOUNS: "
print "ADJECTIVES: "
print "ORIGINAL TWEETS: "
print "TIMES FAVORITED (ORIGINAL TWEETS ONLY): "
print "TIMES RETWEETED (ORIGINAL TWEETS ONLY): "
