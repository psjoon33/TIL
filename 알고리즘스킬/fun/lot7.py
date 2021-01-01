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
        if z == y:
            continue
        cnt = []
        for w in x:
            if w in z:
                cnt.append()