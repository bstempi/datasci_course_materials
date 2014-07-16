import json
import re
import sys

def lines(fp):
    return fp.readlines()

def main():
    tweet_file = open(sys.argv[1])
    tweet_lines = lines(tweet_file)
    hashtag_counts = dict()
    for tweet_line in tweet_lines:
        tweet = json.loads(tweet_line)
        entities = tweet.get('entities', None)
        if not entities:
            continue
        hashtags = entities.get('hashtags', None)
        for hashtag in hashtags:
            try:
                hashtag['text'].decode('ascii')
            except UnicodeEncodeError:
                continue
            if hashtag['text'] not in hashtag_counts:
                hashtag_counts[hashtag['text']] = 0
            hashtag_counts[hashtag['text']] += 1
    sort = dict(sorted(hashtag_counts.iteritems(), key=lambda (k, v): (v, k), reverse=True)[:10])
    for key in sort.keys():
        print "{0} {1}".format(key, hashtag_counts[key])

if __name__ == '__main__':
    main()
