import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    ns = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    a = nums.pop(0)
    b = nums.pop(0)

    results = [{} for _ in range(N-1)]

    for i in range(4):
        if ns[i] > 0:
            ns[i] -= 1

            if i == 0:
                res = a + b
                
            elif i == 1:
                res = a - b

            elif i == 2:
                res = a * b

            elif i == 3:
                res = int(a / b)

            results[0][tuple(ns)] = tuple([res])
            ns[i] += 1
                
    for i in range(N-2):
        x = nums[i]
        for k in results[i]:
            for l in range(len(results[i][k])):
                recent = results[i][k][l]
                k = list(k)

                for j in range(4):
                    if k[j] > 0:
                        k[j] -= 1
                        if j == 0:
                            res = recent + x
                        
                        elif j == 1:
                            res = recent - x

                        elif j == 2:
                            res = recent * x

                        elif j == 3:
                            res = int(recent / x)

                        if tuple(k) not in results[i+1]:
                            tu = tuple([res])
                            results[i+1][tuple(k)] = tu
                        else:
                            if len(results[i+1][tuple(k)]) == 1:
                                results[i+1][tuple(k)] = tuple(sorted(tuple(list(results[i+1][tuple(k)]) + [res])))
                            else:
                                (m, M) = results[i+1][tuple(k)] 
                                if res < m:
                                    results[i+1][tuple(k)] = tuple([res, M])
                                elif res > M:
                                    results[i+1][tuple(k)] = tuple([m, res])

                        k[j] += 1
                k = tuple(k)

    r = results[N-2][(0, 0, 0, 0)]
    if len(r) == 1:
        result = 0
    else:
        result = r[1] - r[0]

    print('#{} {}'.format(tc, result))