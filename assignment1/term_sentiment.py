import json
import re
import sys

def generate_sent_map(sent_lines):
    my_dict = dict()
    for line in sent_lines:
        line_elements = line.split('\t')
        my_dict[line_elements[0]] = int(line_elements[1].strip())
    return my_dict

def score_tweet(tweet_text, sent_map, unknown_map):
    total_score = 0
    words = tweet_text.split(' ')
    unknown_words = []
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
        else:
            unknown_words.append(word)
    for unknown_word in unknown_words:
        unknown_word_map_entry = unknown_map.get(unknown_word, None)
        if unknown_word_map_entry:
            unknown_word_map_entry.append(score)
        else:
            unknown_map[unknown_word] = [score]

def lines(fp):
    return fp.readlines()

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_lines = lines(sent_file)
    tweet_lines = lines(tweet_file)
    sent_map = generate_sent_map(sent_lines)
    unknown_map = dict()
    
    for tweet_line in tweet_lines:
        tweet = json.loads(tweet_line)
        tweet_text = tweet.get('text', None)
        if  tweet_text:
            score_tweet(tweet_text, sent_map, unknown_map)

    # average the tweet score for each unknown word
    for unknown_word in unknown_map.keys():
        scores = unknown_map[unknown_word]
        average = reduce(lambda x, y: x + y, scores) / len(scores)
        if average != 0:
            print '{0:s} {1:d}'.format(unknown_word, average)

if __name__ == '__main__':
    main()
