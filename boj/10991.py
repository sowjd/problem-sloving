n = int(input())

for i in range(n):
    s = " " * (n - i - 1)   # 앞쪽 공백
    while len(s) < n + i:
        if (len(s) - (n + i)) % 2 == 1:
            s += "*"
        else:
            s += " "
    print(s)
