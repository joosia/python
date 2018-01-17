try:
    print hello  # Not defined > NameError
except NameError:
    print "NameError!"

try:
    li = [1,2,3,4]
    print li[4] # The last index is 3 > IndexError
except IndexError:
    print "IndexError!"

try:
    di = {1 : "one", 2 : "two", 3 : "three"}
    print di[4] # Wrong key > KeyError
except KeyError:
    print "KeyError!"
