"""
변을 공유하면 안되니까 대각선으로 선택
 1. 한칸 뒤 대각선
 2. 두칸 뒤 대각선
 (세칸 뒤 대각선 = 한칸 뒤 대각선 * 3 or 한칸 뒤 대각선 + 두칸 뒤 대각선)

d[0][i]: (0, 0)부터 (0, i)까지의 최대합 (i < n)
"""

import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]
    d = [[0] * n for _ in range(2)]

    for i in range(n):

        d[0][i] = arr[0][i]
        d[1][i] = arr[1][i]

        if i == 0:
            continue
        if i == 1:
            d[0][i] += d[1][i-1]
            d[1][i] += d[0][i-1]
        else:
            d[0][i] += max(d[1][i-1], d[1][i-2])
            d[1][i] += max(d[0][i-1], d[0][i-2])
    
    print(max(d[0][-1], d[1][-1]))
