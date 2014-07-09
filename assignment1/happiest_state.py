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

def get_tweet_location(tweet_text):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    words = tweet_text.split(' ')
    for word in words:
        word = word.upper()
        if word in states:
            return word
    return None

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_lines = lines(sent_file)
    tweet_lines = lines(tweet_file)
    sent_map = generate_sent_map(sent_lines)
    state_sentiments = dict()

    for tweet_line in tweet_lines:
        tweet = json.loads(tweet_line)
        tweet_text = tweet.get('text', None)
        if tweet_text:
            location = get_tweet_location(tweet_text)
        if location and tweet_text:
            sentiment = score_tweet(tweet_text, sent_map)
            if not location in state_sentiments:
                state_sentiments[location] = []
            state_sentiments[location].append(sentiment)

    happiest_state = ''
    happiest_state_score = 0
    for state in state_sentiments.keys():
        score = reduce(lambda x, y: x + y, state_sentiments[state]) / len(state_sentiments[state])
        if score > happiest_state_score:
            happiest_state = state
            happiest_state_score = score

    print happiest_state

if __name__ == '__main__':
    main()
