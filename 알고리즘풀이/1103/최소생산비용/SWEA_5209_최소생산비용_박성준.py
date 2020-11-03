import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    results = [{} for _ in range(N)]

    for i in range(N):
        a = arr[0][i]
        b = tuple([i])
        results[0][b] = int(a)

    id = 0
    while id < N:
        for x in results[id]:
            key = list(x)
            val = results[id][x]
            for y in range(N):
                if y not in key:
                    newkey = tuple(sorted(key+[y]))
                    newvalue = val + arr[id+1][y]
                    if newkey in results[id+1]:
                        if newvalue < results[id+1][newkey]:
                            results[id+1][newkey] = newvalue
                    else:
                        results[id+1][newkey] = newvalue
        id += 1

    result = 1000000000000000000000000000000000000
    for x in results[N-1]:
        if results[N-1][x] < result:
            result = results[N-1][x]
    print('#{} {}'.format(tc, result))

