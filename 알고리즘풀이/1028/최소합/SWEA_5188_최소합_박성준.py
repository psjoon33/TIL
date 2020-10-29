import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)

    results = [[0]*N for _ in range(N)]

    results[0][0] = arr[0][0]

    for i in range(1, N):
        results[0][i] = results[0][i-1] + arr[0][i]
        results[i][0] = results[i-1][0] + arr[i][0]
    # print(results)

    for j in range(1, N-1):
        results[j][j] = min(results[j-1][j], results[j][j-1]) + arr[j][j]
        # print(results)
        for k in range(j+1, N):
            results[j][k] = arr[j][k] + min(results[j][k-1], results[j-1][k])
            results[k][j] = arr[k][j] + min(results[k-1][j], results[k][j-1])
        
        result = arr[N-1][N-1] + min(results[N-2][N-1], results[N-1][N-2])

    print('#{} {}'.format(tc, result))



