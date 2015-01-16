#!/usr/bin/env python

# top 25 retweets

import json
import gzip

top = 25

def insert(tweets, tweet):
    if len(tweets) == 0:
        tweets.append(tweet)
    for i in range(0, len(tweets)):
        if tweet['retweet_count'] > tweets[i]['retweet_count']:
            tweets.insert(i, tweet)
            break
    while len(tweets) > top:
        tweets.pop()

tweets = []
for line in gzip.open('tweets.json.gz'):
    tweet = json.loads(line)
    if tweet['retweet_count'] > 0:
        insert(tweets, tweet)

for tweet in tweets:
    print tweet['id'], tweet['retweet_count']
        


