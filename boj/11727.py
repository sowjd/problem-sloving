n = int(input())
d = [0] * 1001

for i in range(1, n + 1):
    if i == 1:
        d[i] = 1
    elif i == 2:
        d[i] = 3
    else:
        d[i] = (d[i - 1] + d[i - 2] * 2) % 10007

print(d[n])
