import sys

d = [0] * 11

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(input())

    for i in range(1, n + 1):
        if d[i] != 0:
            continue

        if i == 1:
            d[i] = 1
        elif i == 2:
            d[i] = 2
        elif i == 3:
            d[i] = 4    # 1+1+1, 1+2, 2+1, 3
        else:
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    print(d[n])
