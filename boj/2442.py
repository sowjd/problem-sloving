"""
별 뒤쪽 공백을 출력하지 않아야 정답..!
"""
n = int(input())

for i in range(1, n + 1):
    s = "*" * (i * 2 - 1)
    print(s.rjust(i + n - 1, " "))  # 별 개수 = 2i -1, 공백 개수 = n - i => (2i -1) + (n - i) = i + n - 1
