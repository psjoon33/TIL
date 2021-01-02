import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

cnt = 0
for i in range(n-80):
    res = {}
    x = a[i]
    y = a[i+1:i+81]
    for z in y:
        inc = []
        for w in x:
            if w in z:
                inc.append(w)
        if len(inc) > 1:
            if tuple(inc) in res:
                res[tuple(inc)] += 1
            else:
                res[tuple(inc)] = 1
    for j in res:
        if res[j] > 1:
            # print(j)
            cnt += 1
            break
print(cnt)

# 최근있었던 80개를 봤을 때 2개가 겹치는 경우가 2개 이상일 확률 98퍼센트