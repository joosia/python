import sys

# Index 0 is the file  A29.py itself
filename = sys.argv[1]
f = open(filename)
content = f.read()
print content
