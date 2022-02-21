#!/usr/bin/env python
"""mapper.py"""

# Author: Victor Hwasser
# Date: 11 feb 2022
# Instructions: Feed a stream of dict/json-objects through stdin to insert it into db

# !! Unfortunatly this instance doesn't have enough RAM to insert each tweet_text_n.txt,
# even seperatly, the instance will be killed by linux after about half is inserted.

import sys
import json
import pymongo
from pymongo import MongoClient
import time

# Count tweets 
print("Start counting tweets")
tweets = []
for line in sys.stdin:
    if line == "\n":
        continue
    
    tweet = json.loads(line)
    tweets.append(tweet)

# Connect to client and import tweets
print("Start importing tweets")
client = MongoClient('localhost', 27017)
with client:
    db = client.test
    col = db.tweets
    col.insert_many(tweets, ordered=False)

print("Inserting complete!")

