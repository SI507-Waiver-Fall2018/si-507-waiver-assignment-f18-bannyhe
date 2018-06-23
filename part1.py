# Name: Mu He
# Uniq: bannyhe
# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
from nltk.corpus import *
from nltk import FreqDist

# Secret user credentials to access Twitter API
consumer_key = 'GPWCIGRd64c41kzZgMnYHncCJ'
consumer_secret = 'rbzLZS6ghHsp5t5nH0PfAo06eJRyKv6YcNmJ8sJJZlVbLyFVhM'
access_token = '766827375677939713-mHOg4ynoeyUYILzuyw22ULr4eTFsNgN'
access_token_secret = 'EfcVh4sVx9Wfmol32oTmbEk2rwoA7nBKFQPecFuBzVf0u'

# Request data
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Input data
input_user = sys.argv[1]
username = api.get_user(input_user)
tweets_num = int(sys.argv[2])

# Request data
word_list = []
public_tweets = api.user_timeline(username.screen_name, count=tweets_num)
ori_tweets = 0
fav_num = 0
retweet_num = 0
special_words = ['http', 'https', 'RT']
dict = {}

# Create dictionary
for tweets in public_tweets:
    tokenized_tweet = nltk.tokenize.word_tokenize(tweets.text)
    #print(tokenized_tweet)
    for token in tokenized_tweet:
        if (token[0].isalpha()) and (token not in special_words):
            if token not in dict:
                dict[token] = 1
            else:
                dict[token] += 1
    try:
        tweet_test = tweets.retweeted_status
    except:
        ori_tweets += 1
        fav_num += tweets.favorite_count
        retweet_num += tweets.retweet_count

# Sort words
sort_key = sorted(list(dict.keys()), key = lambda k: dict[k], reverse = True)

tagged = nltk.pos_tag(sort_key)

verbs = []
nouns = []
adjectives = []

for word in tagged:
    if "VB" in word[1]:
        verbs.append(word[0])
for word in tagged:
    if "NN" in word[1]:
        nouns.append(word[0])
for word in tagged:
    if "JJ" in word[1]:
        adjectives.append(word[0])

# Print out all the information
print("USER: " + username.screen_name)
print("TWEETS ANALYZED: " + str(tweets_num))
str_n = ""
str_v = ""
str_a = ""
for word in range(5):
    str_n += nouns[word] + '(' + str(dict[nouns[word]]) + ')' + " "
    str_v += verbs[word] + '(' + str(dict[verbs[word]]) + ')' + " "
    str_a += adjectives[word] + '(' + str(dict[adjectives[word]]) + ')' + " "
print("VERBS: " + str_v)
print("NOUNS: " + str_n)
print("ADJECTIVES: " + str_a)
print ("ORIGINAL TWEETS: ", ori_tweets)
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", fav_num)
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", retweet_num)


# Make a CSV file and save the 5 most frequent nouns
f = open('noun_data.csv','w')
f.write("Noun, Number\n")
for noun in range(5):
    f.write("{},{}\n".format(nouns[noun], dict[nouns[noun]]))
f.close()
