import sys
sys.stdin = open('input.txt', 'r')

def left(x):
    global goal
    global result
    while True:
        if len(x) == 1 and x[0] == goal:
            result = 1
            break
        # 왼쪽거부터 goal을 찾는 함수
        x = x[ : (len(x)-1)//2]
        # print(x)
        l = len(x)
        if x[(l-1)//2] == goal:
            result = 1
            break
        elif x[(l-1)//2] < goal:
            x = x[(l-1)//2+1:]
            # print(x)
            if x[(len(x)-1)//2] > goal:
                continue
            elif x[(len(x)-1)//2] == goal:
                result = 1
                break
            else:
                result = 0
                break
        else:
            result = 0
            break

def right(x):
    global goal
    global result
    while True:
        if len(x) == 1 and x[0] == goal:
            result = 1
            break
        # 오른쪽거부터 goal을 찾는 함수
        # x = x[ : (len(x)-1)//2]
        x = x[(len(x)-1)//2+1 : ]
        # print(x)
        l = len(x)
        # l = 7
        # [9 10 11 12 13 14 15]

        if x[(l-1)//2] == goal:
            result = 1
            break

        elif x[(l-1)//2] > goal:
            x = x[:(l-1)//2]
            # [9 10 11]
            # print(x)
            if x[(len(x)-1)//2] == goal:
                result = 1
                break
            elif x[(len(x)-1)//2] < goal:
                continue
            else:
                result = 0
                break
        else:
            result = 0
            break




for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # print(A)
    # print(B)

    cnt = 0
    for j in B:
        if j not in A:
            continue
        goal = j
        li = A[:]

        # 시작할 때,,,, goal이 리스트 중간기준 오른쪽에 있을 때,,,,
        if li[len(li)//2] < goal:
            right(li)

        # 시작할 때,,, goal이 왼쪽에 있을 때,,,,
        elif li[len(li)//2] > goal:
            left(li)

        # 만약 바로 중간값이 나오면,,, cnt +1
        else:
            cnt += 1
            continue
        
        cnt += result

        # else:
            # print('shit')

    print('#{} {}'.format(tc, cnt))








