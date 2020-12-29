import sys
sys.stdin = open('로또.txt', 'r')
# 최근 10 번 중에 2개이상 같은 수가 겹치는 지를 확인
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))

result = 0
for i in range(932):
    x = a[i]
    y = a[i+1:i+931]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt >= 5:
            result += 1
            print(i)
            print(x)
            print(z)
            print()
            break
    
print(result)
    
