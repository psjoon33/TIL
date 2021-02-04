import sys
sys.stdin = open('1.txt', 'r')

def e(x):
    return x + 1
def f(x):
    return x - 1
def g(x):
    return 2 * x
def h(x):
    return x - 10

for tc in range(1, int(input()) + 1):
    s, t = map(int, input().split())
    
    current = [s]
    visited = [0] * 1000001
    length = 0
    check = 0
    k = 0
    l = [t+1, t-1, t/2, t+10]
    while check != 1:    
        length += 1
        stack = current[:]
        current = []
        # print(stack)
        while stack != []:
            x = stack.pop()
            if visited[x] == 1:
                continue
            visited[x] = 1
            # print(x)
            a = e(x)
            if a == t:
                check = 1
                break 
            else:
                if a not in stack and visited[a] == 0 and a not in current:
                    current.append(a)

            b = f(x)
            if b == t:
                check = 1
                break 
            else:
                if b not in stack and visited[b] == 0 and b not in current and t +6 > b > 0:
                    current.append(b)

            c = g(x)
            if c == t:  
                check = 1
                break 
            else:
                if c not in stack and visited[c] == 0 and c not in current and c <= 2 * t and c > 0:
                    current.append(c)
            d = h(x)     
            if d == t:  
                check = 1
                break 
            else:
                if d not in stack and visited[d] == 0 and d not in current and d > 0:
                    current.append(d)
            print(current)
            # print(visited)
        # print(current)
    print('#{} {}'.format(tc, length))






