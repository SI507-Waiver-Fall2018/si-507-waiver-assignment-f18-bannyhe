# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here

# usage should be python3 part1.py <username> <num_tweets>

# Get information of arguments
username = sys.argv[1]
tweets_num = sys.argv[2]

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

# Get twwets and a list of words to analyze
word_list = []
public_tweets = api.user_timeline(id=username, count=tweets_num, tweet_mode="extended")
for tweets in public_tweets:
    tokenized_tweet = nltk.tokenize.word_tokenize(tweet._json["full_text"])
    for token in tokenized_tweet:
        word_list.append(token)

# Analyze words
tagged = nltk.pos_tag(word_list)
verbs = []
nouns = []
adjectives = []

for word in tagged:
    if word[1].startswith("VB"):
        verbs.append(word[0])
    elif word[1].startswith("NN"):
        nouns.append(word[0])
    elif word[1].startswith("JJ"):
        adjectives.append(word[0])

# Get word frequency
verbs = word_count(verbs)
nouns = word_count(nouns)
adjectives = word_count(adjectives)

# Sort by frequency and alphabet
verbs = sorted_list(verbs)
nouns = sorted_list(nouns)
adjectives = sorted_list(adjectives)

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

with open('noun_data.csv','w') as f:
    print("Noun", "Number", file=f, sep=",")
    for i in range(5):
        print(nouns[i][0], nouns[i][1], file=f, sep=",")
