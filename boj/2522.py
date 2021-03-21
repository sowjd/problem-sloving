n = int(input())

# sol 1
for i in range(1, n * 2):
    if i <= n:
        print(("*" * i).rjust(n, " "))
    else:
        print(("*" * (n * 2 - i)).rjust(n, " "))

# sol 2
for i in range(1, n+1):
    print(("*" * i).rjust(n, " "))

for i in range(n-1, 0, -1):
    print(("*" * i).rjust(n, " "))
