import sys
sys.stdin = open('로또.txt', 'r')
a = []
n = 944
# n은 몇 회차인지
for i in range(n):
    a.append(list(map(int, input().split('\t'))))
a = a[1:]

def check(x):
    # 25번 내에 겹치는 2개가 없다면 break
    result = '25번 내에 2개가 겹치는 경우가 없다,,'
    y = a[0:26]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt >= 2:
            result = 'Yes'
            break
    print(result)
    # 이전 회차와 3개 이상 겹치면 break
    result = '이전 회차와 3개 이상 겹친다.'
    y = a[0]
    cnt = 0
    for w in x:
        if w in y:
            cnt += 1
    if cnt < 3:
        result = 'Yes' 
    print(result)
    # 2개 겹치는 경우가 최근 8개에서 2번 있으면 break
    result = 'Yes'
    res = {}
    y = a[0:8]
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
            result = '8번 중에 2개 이상 겹치는 경우 2번 이상'
            break
    print(result)
    # 80번 안에 2개 이상 겹치는 경우 2번 미만
    result = '80번 안에 2개 이상 겹치는 경우 2번 미만'
    res = {}
    y = a[0:80]
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
    # 120개를 보면 3개 이상 겹치는 경우가 무조건 있음
    result = '120개에 3개 겹치는경우 없,,'
    y = a[0:120]
    for z in y:
        cnt = 0
        for w in x: 
            if w in z:
                cnt += 1
        if cnt == 3:
            result = 'Yes'
            break
    print(result)
    # 50개를 봤을 때 4개 이상 겹치는 경우 없다.
    result = 'Yes'
    y = a[:50]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt > 3:
            result = '50개 중에 4개 이상 겹친다.'    
            break
    print(result)
    # 4개 이상 겹치는 갯수가 2개 초과인 경우는 없다.
    res = {}
    result = 'Yes'
    y = a[:]
    for z in y:
        if z == x:
            continue
        cnt = []
        for w in x:
            if w in z:
                cnt.append(w)
        if len(cnt) > 3:
            if tuple(cnt) in res:
                res[tuple(cnt)] += 1
            else:
                res[tuple(cnt)] = 1
    count = 0
    for r in res:
        if res[r] > 2:
            result = '4개 이상 겹치는 경우가 2개 초과'
            break
    print(result)
    # 전체에서 5개 이상 겹치는 경우 없다.
    y = a
    result = 'Yes'
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt > 4:
            result = '5개 이상 같다.'
    print(result)


# put = [5, 8, 11, 17, 24, 30]

import random
put = sorted(random.sample(range(1, 46), 6))
put = [2, 13, 16, 19, 32, 33]
print(a[1])
print(a[0])
print(put)
check(put)






