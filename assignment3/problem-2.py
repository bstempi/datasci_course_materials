import MapReduce
import sys
from sets import Set

"""
Problem 1 -- relational join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: table name
    # value: table tuple
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents the word appears in
    order = list_of_values.pop(0)
    for v in list_of_values:
        result = list()
        for i in order:
            result.append(i)
        for i in v:
            result.append(i)
        mr.emit((result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
