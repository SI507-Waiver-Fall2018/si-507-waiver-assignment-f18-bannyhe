# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here

# Step 1 - Twitter data request

# usage should be python3 part1.py <username> <num_tweets>
username = sys.argv[1]
tweets_num = sys.argv[2]

# Secret user credentials to access Twitter API
consumer_key = 'GPWCIGRd64c41kzZgMnYHncCJ'
consumer_secret = 'rbzLZS6ghHsp5t5nH0PfAo06eJRyKv6YcNmJ8sJJZlVbLyFVhM'
access_token = '766827375677939713-mHOg4ynoeyUYILzuyw22ULr4eTFsNgN'
access_token_secret = 'EfcVh4sVx9Wfmol32oTmbEk2rwoA7nBKFQPecFuBzVf0u'

# Request data
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def request(username, tweets_num):
    public_tweets = api.user_timeline(id=username, count=tweets_num, tweet_mode="extended")
    return public_tweets

# Get tweets
tweets_list = []
for tweet in request(username, tweets_num):
    tweets_list.append(tweet.full_text)

tweets = api.search(username)

print("USER: ", username)
print("TWEETS ANALYZED: ", tweets_num)

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
print ("VERBS: ", end=' ')
for word_freq_tuple in sorted_verb_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word, "(" + str(frequency) + ")" , end=' ')
print('')

# Step 4 - Five most common nouns

noun_lst = []

for word_tag_tuple in tag_lst:
    if word_tag_tuple[1][:2] == 'NN':
        noun_lst.append(word_tag_tuple[0])

# Calculate frequency distribution on words
noun_freq_dic = nltk.FreqDist(noun_lst)

# Sort the words by their frequency
sorted_noun_freq_lst = sorted(noun_freq_dic.items(), key = lambda x:x[1], reverse = True)

# Print out the 5 most common words
print("NOUNS: ", end=' ')
for word_freq_tuple in sorted_noun_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word, "(" + str(frequency) + ")", end=' ')
print('')

# Step 5 - Five most frequent adjectives

adj_lst = []

for word_tag_tuple in tag_lst:
    if word_tag_tuple[1][:2] == 'JJ':
        adj_lst.append(word_tag_tuple[0])

# Calculate frequency distribution on words
adj_freq_dic = nltk.FreqDist(adj_lst)

# Sort the words by their frequency
sorted_adj_freq_lst = sorted(adj_freq_dic.items(), key = lambda x:x[1], reverse = True)

# Print the 5 most common words
print ("ADJECTIVES: ", end=' ')
for word_freq_tuple in sorted_adj_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word, "(" + str(frequency) + ")" , end=' ')
print('')

# Get the number of original tweets, favorites, and retweets

# Count original tweets
ori_tweets = 0
ori_tweets_lists = []
ori_tweets_status = []
for tweet in request(name, tweets_num):
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        ori_tweets += 1
        ori_tweets_status.append(tweet)
        ori_tweets_lists.append(tweet.full_text)

ori_fav_count = 0
for tweet in ori_tweets_status:
    ori_fav_count = ori_fav_count + tweet.favorite_count

ori_re_count = 0
for tweet in ori_tweets_status:
    ori_re_count = ori_re_count + tweet.retweet_count

# Print the number of original tweets
print ("ORIGINAL TWEETS: ", ori_tweets)

# Print the number of favorites
print ("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", ori_fav_count)

# Print the number of retweets
print ("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", ori_re_count)


# Make a CSV file of the 5 most frequent nouns

f = open('noun_data.csv','w')
f.write("Noun, Number\n")

for word_freq_tuple in sorted_noun_freq_lst[0:5]:
	word, frequency = word_freq_tuple
	f.write("{},{}\n".format("\"" + word + "\"", "\"" + str(frequency) + "\""))

f.close()
