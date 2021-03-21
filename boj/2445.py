n = int(input())

for i in range(1, n * 2):
    s = ""
    if i <= n:
        s = "*" * i + " " * (n - i)
    else:
        s = "*" * (n * 2 - i) + " " * (i - n)
    print(s + s[::-1])    # s[::-1] 문자열 거꾸로 출력
