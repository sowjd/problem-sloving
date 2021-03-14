"""
print()의 default는 print("출력내용", end="\n") 이다.
"""
import sys

for line in sys.stdin:
    print(line, end="")
