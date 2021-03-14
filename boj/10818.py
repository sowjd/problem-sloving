import sys

sys.stdin.readline()
num = list(map(int, sys.stdin.readline().rstrip().split()))

num.sort()

print(num[0], num[-1])
