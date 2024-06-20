import sys

text = ' '.join(sys.argv[1:])

for c in text:
    print(ord(c), end=' ')

