import json
import re
import sys

def count_tweet(tweet_text, count_map):
    total = 0
    words = tweet_text.split(' ')
    for word in words:
        word = word.lower()
        word = re.sub(r'\W+', '', word)
        if not word:
            continue
        try:
            word.decode('ascii')
        except UnicodeEncodeError:
            continue
        count_entry = count_map.get(word, 0)
        count_map[word] = count_entry + 1
        total += 1
    return total

def lines(fp):
    return fp.readlines()

def main():
    tweet_file = open(sys.argv[1])
    tweet_lines = lines(tweet_file)
    count_map = dict()
    count_total = 0
    
    for tweet_line in tweet_lines:
        tweet = json.loads(tweet_line)
        tweet_text = tweet.get('text', None)
        if  tweet_text:
            count_total += count_tweet(tweet_text, count_map)

    for key in count_map.keys():
        entry = count_map[key]
        print '{0:s} {1:20.20f}'.format(key, entry/float(count_total))

if __name__ == '__main__':
    main()
