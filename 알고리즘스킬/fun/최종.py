import sys
sys.stdin = open('로또.txt', 'r')
a = []
n = 942
# n은 몇 회차인지
for i in range(n):
    a.append(list(map(int, input().split('\t'))))

def check(lot):
    # 25번 내에 겹치는 2개가 없다면 break
    global n
    result = '25번 내에 2개가 겹치는 경우가 없다,,'
    for i in range(n-25):
        x = a[i]
        y = a[i+1:i+26]
        for z in y:
            cnt = 0
            for w in x:
                if w in z:
                    cnt += 1
            if cnt >= 2:
                result = 'Yes'
                break
        if result == 'Yes':
            break
        else:
            print(result)
            break
    # 






