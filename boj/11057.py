# d[n][i]: i로 끝나는 길이가 n인 오르막 수의 개수

n = int(input())
d = [[0] * 10 for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(0, 10):
        if i == 1:      # initalization
            d[1][j] = 1
        else:
            d[i][j] = sum(d[i-1][:j+1]) % 10007

print(sum(d[n]) % 10007)
