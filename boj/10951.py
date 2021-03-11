import sys

for line in sys.stdin:
    print(sum(list(map(int, line.rstrip().split()))))
