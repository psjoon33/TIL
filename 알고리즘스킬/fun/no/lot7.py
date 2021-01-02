import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

result = {}
for i in range(n):
    x = a[i]
    y = a[:]
    for z in y:
        if z == x:
            continue
        cnt = []
        for w in x:
            if w in z:
                cnt.append(w)
        if len(cnt) > 3:
            if tuple(cnt) in result:
                result[tuple(cnt)] += 1
            else:
                result[tuple(cnt)] = 1
count = 0
for r in result:
    if result[r] >2:
        count += 1
print(count)

# 4개 이상 겹치는 갯수가 2개 이상인 경우는 없다.
