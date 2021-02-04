import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    cnt = 0
    for goal in B:
        if goal not in A:
            continue
        r = A.index(goal)
        a = [i for i in range(N)]
        # 같다면
        if a[(len(a)-1)//2] == r:
            cnt += 1
            continue

        # 오른쪽에 있다면
        if a[(len(a)-1)//2] < r:
            while True:
                if len(a) == 0:
                    break
                if a == [r]:
                    cnt += 1
                    break
                a = a[(len(a)-1)//2+1:]
                if r == a[(len(a)-1)//2]:
                    cnt += 1
                    break
                # 왼쪽에 있다면
                elif a[(len(a)-1)//2] > r:
                    a = a[:(len(a)-1)//2]
                    if a[(len(a)-1)//2] == r:
                        cnt += 1
                        break
                    elif a[(len(a)-1)//2] < r:
                        continue
                    else:
                        break
                else:
                    break
        # 왼쪽에 있다면
        if a[(len(a)-1)//2] > r:
            while True:
                if len(a) == 0:
                    break
                if a == [r]:
                    cnt += 1
                    break
                a = a[:(len(a)-1)//2]
                if r == a[(len(a)-1)//2]:
                    cnt += 1
                    break
                # 오른쪽에 있다면
                elif a[(len(a)-1)//2] < r:
                    a = a[(len(a)-1)//2 + 1:]
                    if a[(len(a)-1)//2] == r:
                        cnt += 1
                        break
                    elif a[(len(a)-1)//2] > r:
                        continue
                    else:
                        break
                else:
                    break


    print('#{} {}'.format(tc, cnt))
