import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))

result = 0
for i in range(942):
    x = a[i]
    y = a[i+1:i+2]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt >= 3:
            result += 1
            print(i)
            print(x)
            print(z)
            print()
            break
print(result)

# 이전 회차의 것과 3개 이상 겹치는 경우 = 2퍼센트 뺀다.







