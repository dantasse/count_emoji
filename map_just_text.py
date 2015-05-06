#!/usr/bin/python
# Run this by submitting an AWS EMR streaming job w/ flags:
# -input=input location on S3
# -output=output location on S3
# -mapper=name of the mapper executable
# -reducer=name of the reducer executable
# executables: BucketName/path/MapperExecutable
# also, geez, python on EMR is only 2.6.9, so no Counter.
# http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/ami-versions-supported.html

import sys, csv, re, collections

# emoji_symbols_pictograms = re.compile(u'[\U0001f300-\U0001f5fF]')
# emoji_emoticons = re.compile(u'[\U0001f600-\U0001f64F]')
# emoji_transport_maps = re.compile(u'[\U0001f680-\U0001f6FF]')
# emoji_symbols = re.compile(u'[\U00002600-\U000026FF]')
# emoji_dingbats = re.compile(u'[\U00002700-\U000027BF]')
# all_emoji = re.compile(u'([\U00002600-\U000027BF]|[\U0001f300-\U0001f64F]|[\U0001f680-\U0001f6FF])')
# Python 2, not 3. 3 handles wide unicode characters better. But on 2, we have
# to deal with them as byte sequences and make a regex to catch each 2-byte emoji.

# Returns a list of all the emoji in this string.
# Returns a list because converting them back to characters is
# a big pain.
def get_emoji(text):
    return narrow.findall(text.decode("UTF-8"))

def main(argv):
    narrow = re.compile(u'(\ud83c[\udf00-\udfff]|\ud83d[\udc00-\ude4f\ude80-\udeff]|[\u2600-\u26FF\u2700-\u27BF])')
    try:
        while True:
            line = sys.stdin.readline()
            line = line.strip()
            if line == '':
                break
            emojis = narrow.findall(line.decode("UTF-8"))
            emoji_counter = collections.defaultdict(int)
            # can't use Counter, python 2.6 only.
            for emoji in emojis:
                emoji_counter[emoji] += 1
            print(list(emoji_counter.values()))
    except "end of file": # copied from EMR wordcount example app
        return None

if __name__ == "__main__":
   main(sys.argv)

