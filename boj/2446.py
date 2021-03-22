# 모래시계 모양 출력

n = int(input())

for i in range(n, 1, -1):
    print(("*" * (2 * i - 1)).rjust(n + i - 1, " "))

for i in range(1, n + 1):
    print(("*" * (2 * i - 1)).rjust(n + i - 1, " "))
