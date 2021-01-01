import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

cnt = 0
for i in range(n-25):
    result = {}
    x = a[i]
    y = a[i+1:i+9]
    for z in y:
        inc = []
        for w in x:
            if w in z:
                inc.append(w)
        if len(inc) > 1:
            if tuple(inc) in result:
                result[tuple(inc)] += 1
            else:
                result[tuple(inc)] = 1
    for j in result:
        if result[j] > 1:
            print(j)
            cnt += 1
            break
print(cnt)

# 최근있었던 8개에서 겹치는게 2개있는 확률은 3퍼센트.
# 





