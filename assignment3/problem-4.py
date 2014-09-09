import MapReduce
import sys
from sets import Set

"""
Problem 4 -- asymmetric friends
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: some friend
    # value: some friend

    # ordering is important
    if record[0] < record[1]:
        key = record[0]
        value = record[1]
    else:
        key = record[1]
        value = record[0]

    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: a friend
    # value: list of friends; possibly including dups.  Dup indicates symmetrical relationship

    list_of_values.sort()
    lastFriend = None
    for friend in list_of_values:
        if lastFriend == None:
            lastFriend = friend
        elif lastFriend != friend:
            mr.emit((key, lastFriend))
            mr.emit((lastFriend, key))
            lastFriend = friend
        else:
            lastFriend = None

    # Edge case:  last item needs to be evaluated
    if lastFriend != None:
        mr.emit((key, lastFriend))
        mr.emit((lastFriend, key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
