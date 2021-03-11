import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    result = sum(list(map(int, sys.stdin.readline().rstrip().split())))
    print("Case #", (i+1),  ": ", result, sep="")
    # print("Case #{}: {}".format(i+1, result))   format을 쓰는 방법도 있다.
