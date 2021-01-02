import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

result = 0
for i in range(n-120):
    x = a[i]
    y = a[i+1:i+121]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt > 2:
            result += 1
            # print(i)
            break
print(result)

# 120개를 보면 3개 이상 겹치는 경우가 무조건 있음





