import sys
sys.stdin = open('input.txt','r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    arr = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    invited = arr[1] + [1]

    cnt = len(invited)
    added = []
    for x in invited:
        for y in arr[x]:
            if y not in invited:
                if y not in added:
                    added.append(y)

    cnt += len(added)-1
    print('#{} {}'.format(tc, cnt))




