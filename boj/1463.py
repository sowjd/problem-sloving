"""
모든 n, d[n] = d[n-1] + 1
2의 배수인 n, d[n] = d[n//2] + 1
3의 배수인 n, d[n] = d[n//3] + 1
"""
n = int(input())

d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    if i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])

print(d[n])
