import sys

for line in sys.stdin:
    '''
    문제의 조건: 0 < A, B < 10인 두 정수
    원래 코드가 A = 1, B = -1일 때도 종료되서 수정함
    '''
    #result = sum(list(map(int, line.rstrip().split())))
    a, b = map(int, line.rstrip().split())
    
    # if result == 0:
    if a == 0 and b == 0:
        break
    print(a+b)
