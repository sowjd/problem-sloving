n = int(input())

# sol 1
for i in range(1, n):
    s = " " * (n - i) + "*" + " " * (2 * i - 1 - 2) + "*"
    if i == 1:
        print(s[:-1])
    else:
        print(s)
print("*" * (2 * n - 1))


# sol 2
print(" " * (n - 1) + "*")

if n == 1:
    quit()

for i in range(2, n):
    s = " " * (n - i) + "*" + " " * (2 * i - 1 - 2) + "*"
    print(s)
print("*" * (2 * n - 1))
