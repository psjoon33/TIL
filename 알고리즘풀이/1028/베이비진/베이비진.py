import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    x = []
    y = []
    result = 0
    for z in range(2):
        x.append(arr.pop(0))
        y.append(arr.pop(0))
    for i in range(4):
        x.append(arr.pop(0))
        y.append(arr.pop(0))
        x.sort()
        for k in range(x[0], x[-3]):
            if k in x and (k+1) in x and (k+2) in x:
                result = 1
                break
        if result != 0:
            break

        for j in range(i):
            if x.count(x[j]) == 3:
                result = 1
                break
            elif y.count(y[j]) == 3:
                result = 2
                break
        if result != 0:
            break

        y.sort()
        for l in range(y[0], y[-3]):
            if l in y and (l+1) in y and (l+2) in y:
                result = 2
        if result != 0:
            break
        

        if result != 0:
            break

    print('#{} {}'.format(tc, result))










