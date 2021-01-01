import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

result = 0

for i in range(n):
    x = a[i]
    y = a
    for z in y:
        if z != x:
            cnt = 0
            for w in x:
                if w in z:
                    cnt += 1
            if cnt > 4:
                result += 1
                # print(i)
print(result)

# 전체를 봤을 때 5개 이상 겹치는 경우 없다.