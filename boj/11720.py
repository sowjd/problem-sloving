"""
list(map(int, sys.stdin.readline().rstrip()))
12345 => [1, 2, 3, 4, 5]
"""
import sys

sys.stdin.readline()
print(sum(list(map(int, sys.stdin.readline().rstrip()))))
