import sys

str = ''

for i in sys.argv[1:]:
    str += chr(int(i))

print(str)
