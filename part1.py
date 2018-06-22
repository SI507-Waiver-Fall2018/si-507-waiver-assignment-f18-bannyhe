# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
from nltk.corpus import *
from nltk import FreqDist

# Find word frequency
def word_count(word_lst):
    unique_words = set(word_lst)
    output = []
    if len(unique_words) < len(word_lst):
        for word in unique_words:
            freq = (word, word_lst.count(word))
            output.append(freq)
    return output

# Sort the list by frequency and alphabet
def sorted_list(input_list):
    return sorted(input_list, key = lambda x: (-x[1], x[0]))

# Print out the top 5 words and counts
def top_five(part_of_speech, input_list):
    output = part_of_speech
    for i in range(5):
        output += " " + input_list[i][0] + "(" + str(input_list[i][1]) + ")"
    print(output)

# Secret user credentials to access Twitter API
consumer_key = 'GPWCIGRd64c41kzZgMnYHncCJ'
consumer_secret = 'rbzLZS6ghHsp5t5nH0PfAo06eJRyKv6YcNmJ8sJJZlVbLyFVhM'
access_token = '766827375677939713-mHOg4ynoeyUYILzuyw22ULr4eTFsNgN'
access_token_secret = 'EfcVh4sVx9Wfmol32oTmbEk2rwoA7nBKFQPecFuBzVf0u'

# Request data
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get information of arguments
input_user = sys.argv[1]
username = api.get_user(input_user)
tweets_num = int(sys.argv[2])
special_words = ['http', 'https', 'RT']
dict = {}

# Get tweets and a list of words to analyze
word_list = []
public_tweets = api.user_timeline(user.screen_name, count=tweets_num)
for tweets in public_tweets:
    tokenized_tweet = nltk.tokenize.word_tokenize(tweet.text)
    #print(tokenized_tweet)
    for token in tokenized_tweet:
        if (token[0].isalpha()) and (token not in special_words):
            dict[token] = 1
        else:
            dict[token] += 1

# Sort words
sort_key = sorted(list(dict.keys()), key = lambda x: dict[k], reverse = True)

# Analyze words
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

# Get word frequency
verbs = word_count(verbs)
nouns = word_count(nouns)
adjectives = word_count(adjectives)

# Sort by frequency and alphabet
verbs = sorted_list(verbs)
nouns = sorted_list(nouns)
adjectives = sorted_list(adjectives)

def request(username, tweets_num):
    public_tweets = api.user_timeline(id=username, count=tweets_num, tweet_mode="extended")
    return public_tweets

# Get tweets
tweets_list = []
for tweet in request(username, tweets_num):
    tweets_list.append(tweet.full_text)

tweets = api.search(username)

print("USER: ", username.screen_name)
print("TWEETS ANALYZED: ", str(tweets_num))

# Step 2 - Analyze Tweets

word_lst = [] # List to store words
ignore_lst = ["http","https","RT"] # List of words to be ignored

from nltk.tokenize import word_tokenize

# Read through each tweet, and add the real words into word_lst
for tweet in tweet_list:
    tokenized_text = word_tokenize(tweet) # tokenize the words in the tweet

    # Iterate through each word in tokenized text & filter out the word if it's a stop word
    for word in tokenized_text:
        # Check if the word starts with an alphabetic character [a-z/A-Z], and if it is not in ignore_lst
        if word[0].isalpha() and word not in ignore_lst:
            word_lst.append(word) # Add the word to word_lst

tag_lst = nltk.pos_tag(word_lst)

# Step 3 - Five most frequent verbs

verb_lst = []

for word_tag_tuple in tag_lst:
    if word_tag_tuple[1][:2] == 'VB':
        verb_lst.append(word_tag_tuple[0])

# Count the frequency distribution on word
verb_freq_dic = nltk.FreqDist(verb_lst)

# Sort the words by their frequency
sorted_verb_freq_lst = sorted(verb_freq_dic.items(), key=lambda x:x[1], reverse = True)

# Print the 5 most common words
print("VERBS: ", end=' ')
for word_freq_tuple in sorted_verb_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word, "(" + str(frequency) + ")" , end=' ')
print('')

# Step 4 - Five most common nouns

ori_tweets = 0
fav_num = 0
retweet_num = 0
for tweet in tweets:
    if not tweet._json["retweeted"]:
        ori_tweets += 1
        fav_num += tweet._json["favorite_count"]
        retweet_num += tweet._json["retweet_count"]

# Print out all the information
print("USER: ", username)
print("TWEETS ANALYZED: ", tweets_num)
top_five("VERBS: ", verbs)
top_five("NOUNS: ", nouns)
top_five("ADJECTIVES: ", adjectives)
print ("ORIGINAL TWEETS: ", ori_tweets)
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", fav_num)
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", retweet_num)


# Make a CSV file and save the 5 most frequent nouns
f = open('noun_data.csv','w')
f.write("Noun", "Number\n")
for noun in range(5):
    f.write("{},{}\n".format(noun[i][0], noun[i][1]))
f.close()
