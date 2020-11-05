import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    # N = 2 (0 ~ 2)
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        arr[a][b] = c
        arr[b][a] = c
    # print(arr)

    results = [{} for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N+1):
            if arr[i][j] != 0 :
                x = (i, j)
                results[0][x] = arr[i][j]
    # print(results)

    cnt = 1

    while cnt != N and N > 1:
        for x in results[cnt-1]:
            # x = (0, 1)
            y = results[cnt-1][x]
            # y = 1
            for i in x:
                for j in range(N+1):
                    if j not in x and arr[i][j] != 0:
                        z = tuple(sorted(list(x)+[j]))
                        if z not in results[cnt]:
                            results[cnt][z] = y + arr[i][j]
                        else:
                            w = y + arr[i][j]
                            a = results[cnt][z]
                            if results[cnt][z] > w:
                                results[cnt][z] = w
                        # results[cnt][tuple(sorted(list(x)+[j]))] = y + arr[i][j]
        cnt += 1

    print(results)
    for r in results[-1]:
        result = results[-1][r]

    print('#{} {}'.format(tc, result))




