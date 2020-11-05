import sys
sys.stdin = open('1.txt', 'r')

def cal(arr, results, i, j):
    a = results[i-1][j] + 1
    h = arr[i][j] - arr[i-1][j]
    if h > 0:
        a += h
    b = results[i][j-1] + 1
    h = arr[i][j] - arr[i][j-1]
    if h > 0 :
        b += h

    results[i][j] = min(a, b)




for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    results = [[0]*N for _ in range(N)]

    for i in range(1, N):
        results[0][i] = results[0][i-1] + 1
        h = arr[0][i] - arr[0][i-1]
        if h > 0:
            results[0][i] += h

        results[i][0] = results[i-1][0] + 1
        h = arr[i][0] - arr[i-1][0]
        if h > 0:
            results[i][0] += h
    print(results)

    for i in range(1, N):
        a = results[i-1][i] + 1
        h = arr[i][i] - arr[i-1][i]
        if h > 0:
            a += h
        b = results[i][i-1] + 1
        h = arr[i][i] - arr[i][i-1]
        if h > 0:
            b += h
        results[i][i] = min(a, b)
        





    print(results)
