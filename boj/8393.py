import sys

n = int(sys.stdin.readline().rstrip())

print(sum([i + 1 for i in range(n)]))
