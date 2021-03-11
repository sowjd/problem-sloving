import sys

for line in sys.stdin:
    result = sum(list(map(int, line.rstrip().split())))
    if result == 0:
        break
    print(result)
