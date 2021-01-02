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
    print(result)
    # 이전 회차와 3개 이상 겹치면 break
    result = '이전 회차와 3개 이상 겹친다.'
    for i in range(n-1):
        x = a[i]
        y = a[i+1]
        cnt = 0
        for w in x:
            if w in y:
                cnt += 1
        if cnt < 3:
            result = 'Yes' 
            break
    print(result)
    # 2개 겹치는 경우가 최근 8개에서 2번 있으면 break
    result = 'Yes'
    for i in range(n-8):
        res = {}
        x = a[i]
        y = a[i+1:i+9]
        for z in y:
            inc = []
            for w in x:
                if w in z:
                    inc.append(w)
        if len(inc) > 1:
            if tuple(inc) in res:
                result[tuple(inc)] += 1
            else:
                result[tuple(inc)] = 1
    for j in res:
        if res[j] > 1:
            result = '8번 중에 2개 이상 겹치는 경우 2번 이상'
            break
    print(result)
    # 80번 안에 2개 이상 겹치는 경우 2번 미만
    result = '80번 안에 2개 이상 겹치는 경우 2번 미만'
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
                result = 'Yes'
                break
    print(result)
























