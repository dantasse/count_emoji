#!/usr/bin/env python

# Looks like this is working. Spark still runs python2 :-/ but it at least 
# mostly works. Got slight inconsistencies vs. the python3 emoji-find regex
# but whatever, close enough.
# Also, I can run this locally:
# spark-submit --master local[4] spark.py
import sys, re
from collections import Counter
from pyspark import SparkContext

inputFile = "/Users/dtasse/Desktop/tweet_pgh_small.csv"
# inputFile = "tweet_pgh_sample.csv"
sc = SparkContext("local", "trying out spark")
inputData = sc.textFile(inputFile).cache()

# emoji_symbols_pictograms = re.compile(u'[\U0001f300-\U0001f5fF]')
# emoji_emoticons = re.compile(u'[\U0001f600-\U0001f64F]')
# emoji_transport_maps = re.compile(u'[\U0001f680-\U0001f6FF]')
# emoji_symbols = re.compile(u'[\U00002600-\U000026FF]')
# emoji_dingbats = re.compile(u'[\U00002700-\U000027BF]')
# all_emoji = re.compile(u'([\U00002600-\U000027BF]|[\U0001f300-\U0001f64F]|[\U0001f680-\U0001f6FF])')
# Python 2, not 3. 3 handles wide unicode characters better. But on 2, we have
# to deal with them as byte sequences and make a regex to catch each 2-byte emoji.
narrow = re.compile(u'(\ud83c[\udf00-\udfff]|\ud83d[\udc00-\ude4f\ude80-\udeff]|[\u2600-\u26FF\u2700-\u27BF])')

# Returns a list of all the emoji in this string.
# Returns a list because converting them back to characters is
# a big pain.
def get_emoji_counts(text):
    # emojis = narrow.findall(text.decode("UTF-8"))
    emojis = narrow.findall(text)
    counts = Counter(emojis)
    return counts.values()

emojis = inputData.map(get_emoji_counts)
all_emojis = emojis.reduce(lambda a, b: a + b)
print Counter(all_emojis)
