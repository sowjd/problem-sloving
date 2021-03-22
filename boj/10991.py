"""
Idea
앞쪽 공백 설정 후, 총 길이만큼 * -> " " -> * -> " " -> ... 순서로 더해준다.

n = 4       i   총 길이(n+i)
---*        0       4
--*-*       1       5
-*-*-*      2       6
*-*-*-*     3       7
"""
n = int(input())

for i in range(n):
    s = " " * (n - i - 1)   # 앞쪽 공백
    while len(s) < n + i:
        if (len(s) - (n + i)) % 2 == 1:
            s += "*"
        else:
            s += " "
    print(s)
