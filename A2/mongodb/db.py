import pymongo
import re
import bson
import sys

# Author: Victor Hwasser
# Date: 13 feb 2022

# Connect to collection
client = pymongo.MongoClient('localhost', 27017) 
db = client["test"]
col = db["tweets"]

print("Start counting words")

regx = bson.regex.Regex(r'\bhan\b')
regx.flags ^= re.IGNORECASE
han = col.count_documents({'text': regx})
print("Done with 1/7")

regx = bson.regex.Regex(r'\bhon\b')
regx.flags ^= re.IGNORECASE
hon = col.count_documents({'text': regx})
print("Done with 2/7")

regx = bson.regex.Regex(r'\bhen\b')
regx.flags ^= re.IGNORECASE
hen = col.count_documents({'text': regx})
print("Done with 3/7")

regx = bson.regex.Regex(r'\bden\b')
regx.flags ^= re.IGNORECASE
den = col.count_documents({'text': regx})
print("Done with 4/7")

regx = bson.regex.Regex(r'\bdet\b')
regx.flags ^= re.IGNORECASE
det = col.count_documents({'text': regx})
print("Done with 5/7")

regx = bson.regex.Regex(r'\bdetta\b')
regx.flags ^= re.IGNORECASE
denna = col.count_documents({'text': regx})
print("Done with 6/7")

regx = bson.regex.Regex(r'\bdenne\b')
regx.flags ^= re.IGNORECASE
denne = col.count_documents({'text': regx})
print("Done with 7/7")

# Write the result to a file
sys.stdout = open('results.txt', 'w')
print("%s\t%s" % ('han', han))
print("%s\t%s" % ('hon', hon))
print("%s\t%s" % ('hen', hen))
print("%s\t%s" % ('den', den))
print("%s\t%s" % ('det', det))
print("%s\t%s" % ('denna', denne))
print("%s\t%s" % ('denne', denna))
sys.stdout.close()
