# d[n][i] : i로 끝나는 길이가 n인 계단수의 개수

n = int(input())
d = [[0] * 10 for _ in range(n + 1)]

# initalization
for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][j + 1]
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = (d[i - 1][j + 1] + d[i - 1][j - 1]) % (10 ** 9)

print(sum(d[n]) % (10 ** 9))
