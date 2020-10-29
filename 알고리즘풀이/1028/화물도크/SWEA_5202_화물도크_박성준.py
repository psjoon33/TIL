import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr = [[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]]

    visited = []

    m = 100
    for a in arr:
        if a[1] < m:
            m = a[1]
            recent = a
    arr.remove(recent)
    print(arr)
    # arr = [[20, 23], [17, 20], [23, 24], [8, 18]]
    # m = 14
    cnt = 1

    while True:
        r = []
        for a in arr:
            if  m <= a[0]:
                r.append(a)
        # print(r)
        # [[20, 23], [17, 20], [23, 24]]
        if r == []:
            break

        n = 10000
        for x in r:
            if x[1] < n:
                n = x[1]
                k = x
        
        # k = [17, 20]
        m = k[1]
        cnt += 1
    print('#{} {}'.format(tc, cnt))








