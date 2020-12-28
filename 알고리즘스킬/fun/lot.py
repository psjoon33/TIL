import sys
sys.stdin = open('로또.txt', 'r')
# 최근 10 번 중에 2개이상 같은 수가 겹치는 지를 확인
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))

for i in range(10, 942):
    x = a[i]
    y = a[i-10:i]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                