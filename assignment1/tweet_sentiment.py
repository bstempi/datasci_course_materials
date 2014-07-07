import json
import re
import sys

def generate_sent_map(sent_lines):
    my_dict = dict()
    for line in sent_lines:
        line_elements = line.split('\t')
        my_dict[line_elements[0]] = int(line_elements[1].strip())
    return my_dict

def lines(fp):
    return fp.readlines()

def score_tweet(tweet_text, sent_map):
    total_score = 0
    words = tweet_text.split(' ')
    for word in words:
        word = word.lower()
        word = re.sub(r'\W+', '', word)
        try:
            word.decode('ascii')
        except UnicodeEncodeError:
            continue
        score = sent_map.get(word, 0)
        if score:
            total_score += score
    return total_score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_lines = lines(sent_file)
    tweet_lines = lines(tweet_file)
    sent_map = generate_sent_map(sent_lines)

    for tweet_line in tweet_lines:
        tweet = json.loads(tweet_line)
        tweet_text = tweet.get('text', None)
        if not tweet_text:
            print 0
        else:
            print score_tweet(tweet_text, sent_map)

if __name__ == '__main__':
    main()
