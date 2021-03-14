"""
몫만 구하는 나누기 연산자는 // 이다.
문자열을 자를 때 끝 인덱스는 out of index라도 에러가 발생하지 않는다. (유연하게 처리)
"""
import sys

line = sys.stdin.readline().rstrip()

for i in range(len(line) // 10 + 1):
    print(line[i * 10 : (i + 1) * 10])
