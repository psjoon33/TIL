import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))
n = len(a)

result = 0
for i in range(n-25):
    x = a[i]
    y = a[i+1:i+26]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt >= 2:
            result += 1
            print(i)
            print(x)
            print(z)
            print()
            break
print(result)

# 최근 있었던 25개를 봤을 때 최소 1번의 케이스에 한해서 2개 이상의 숫자가 겹친다.
# 약98퍼센트