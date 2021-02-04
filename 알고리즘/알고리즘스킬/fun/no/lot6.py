import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

result = 0

for i in range(n-51):
    x = a[i]
    y = a[i+1:i+51]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt > 3:
            result += 1
            print(i)
print(result)

# 50개를 봤을 때 4개 이상 겹치는 경우 없다.



