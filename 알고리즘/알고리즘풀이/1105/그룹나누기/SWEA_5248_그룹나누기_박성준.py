import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    connected = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = arr[2*i], arr[2*i+1]
        connected[a].append(b)
        connected[b].append(a)
    # print(connected)

    
    results = []
    stack = []
    visited = []
    # results

    for i in range(1, N+1):
        if i not in visited:
            results.append([i])
            stack.append(i)
            # print(results)
            while len(stack) > 0:
                a = stack.pop()
                visited.append(a)
                for x in connected[a]:
                    if x not in stack and x not in visited:
                        stack.append(x)
                        results[-1].append(x)

    print('#{} {}'.format(tc, len(results)))




