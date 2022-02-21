#!/usr/bin/env python
"""mapper.py"""

import sys
import json

# list of prenouns
pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]

# convert all input into a list of JSON-objects

for line in sys.stdin:
    if line == "\n":
        continue

    tweet = json.loads(line)

    # it this is a retweet, ignore it
    if tweet["retweeted"] == True:
        continue

    # format the text for iterating through
    tweet_words = tweet["text"].lower()
    tweet_words = tweet_words.split()

    # instead of testing word by word in tweet, check list of prenouns
    # and if any of these are inside the tweet. This way we avoid doubles.
    for word in pronouns:
        # check if tweet contain pronoun
        if word in tweet_words:
            print('%s\t%s' % (word, 1))

    # Print all unique tweets
    print('tweet\t1')
