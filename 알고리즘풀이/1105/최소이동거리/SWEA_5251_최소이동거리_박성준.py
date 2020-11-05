import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    arr = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a][b] = c

    status = [0]

    current = []
    
    results = []

    m = 100000000000000000000000000000000000

    for i in range(1, N+1):
        if arr[0][i] != 0:
            if i == N:
                results.append(status + [i])
            else:
                k = arr[0][i]
                current.append(status + [i] +[k])

    if results != []:
        a = arr[0][N]
        if m > a:
            m = a

    for i in range(N-1):
        status = current[:]
        current = []
        while status != []:
            x = status.pop()
            hap = x.pop()
            y = x[-1]

            for z in range(N+1):
                if z not in x and arr[y][z] != 0:
                    if z == N:
                        sub = hap + arr[y][N]
                        if m > sub:
                            m = sub
                    else:
                        sub = hap + arr[y][z]
                        if m < sub:
                            continue
                        else:
                            current.append(x + [z] + [sub])

    print('#{} {}'.format(tc, m))
    



