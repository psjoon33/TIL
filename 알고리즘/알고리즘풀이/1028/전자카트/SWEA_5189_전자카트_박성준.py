import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    X = int(input())
    # X = 3
    arr = [list(map(int, input().split())) for _ in range(X)]
    print(arr)
    numbers = [i for i in range(2, X+1)]
    print(numbers)
    N = X - 1
    # N = 2

    sel = [0] * N
    visited = [0]*N
    sels = []
    m = 10000000000000


    # numbers = [2, 3]
    def perm(idx):
        global m
        if idx == N:
            
            a = [1] + sel + [1]
            res = 0
            print(a)
            for k in range(X):
                print(k)
                res += arr[a[k]-1][a[k+1]-1]
            if m > res:
                m = res
            return
        else:
            for i in range(N):
                if not visited[i]:
                    visited[i] = 1
                    sel[i] = numbers[idx]
                    perm(idx+1)
                    visited[i] = 0
    perm(0)

    print('#{} {}'.format(tc, m))
