import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    results = [{} for _ in range(N)]

    for i in range(N):
        results[0][tuple([i])] = arr[0][i]
    # print(results)

    id = 0
    while id <N-1:
        for x in results[id]:
            key = list(x)
            val = results[id][x]
            for y in range(N):
                if y not in key:
                    if arr[id+1][y] == 0:
                        continue
                    newkey = tuple(sorted(key+[y]))
                    newval = arr[id+1][y] * val
                    if newkey in results[id+1]:
                        if newval > results[id+1][newkey]:
                            results[id+1][newkey] = newval
                    else:
                        results[id+1][newkey] = newval                                
        id += 1

    for i in results[N-1]:
        result = results[N-1][i]

    result = result * (10**(-2*(N-1)))

    # if '.' not in result:
    #     result += '.' + '0'*6
    # else:
    #     ind = result.index('.')
    #     need = 6 - len(result[ind+1:])
    #     result = result + '0' * need

    print('#{} {:.6f}'.format(tc, result))
