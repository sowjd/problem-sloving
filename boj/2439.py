import sys

n = int(sys.stdin.readline().rstrip())

# sol 1
for i in range(n):
    print("{}{}".format(" " * (n - i - 1), "*" * (i + 1)))

# sol 2
for i in range(n):
    print(("*" * (i + 1)).rjust(n))
