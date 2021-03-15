import sys
sys.stdin = open('l.txt', 'r')

a = []
n = 953
# n은 몇 회차인지

for i in range(n):
    # a.append(list(map(int, input().split('\t'))))
    a = [list(map(int, input().split('\t')))] + a

# 룰에 어긋나는 경우의 카운트를 result
result = []

# 1. 같은 수가 4번 연속 나오는 경우는 없다. 
for i in range(120, n):
    current = a[i]
    past = a[i-3:i]
    for x in current:
        if x in past[0] and x in past[1] and x in past[2]:
            result.append(i)
            continue

# 2. 이전 회차와 3개 이상 겹치는 경우는 없다.
    past = a[i-1]
    cnt = 0
    for x in current:
        if x in past:
            cnt += 1
    if cnt >= 3:
        result.append(i)
        continue

# 3. 최근 56개를 봤을 때 4개 이상 겹치는 경우는 없다.
    past = a[i-56:i]
    for x in past:
        cnt = 0
        for y in current:
            if y in x:
                cnt += 1
        if cnt > 3:
            break
    if cnt > 3:
        result.append(i)
        continue
            
# 4. 5개 이상 겹치는 경우 없다.            
    for x in a:
        if x == current:
            continue
        cnt = 0
        for y in current:
            if y in x:
                cnt += 1
        if cnt > 4:
            break
    if cnt > 4:
        result.append(i)
        continue

# 5. 최근 3번에서 2번 이상 등장했던 숫자 쌍이 2개 이상인 경우는 없다.
    past = a[i-3:i]
    check = [0 for _ in range(46)]
    for x in past:
        for y in current:
            if y in x:
                check[y] += 1
    cnt = 0
    for c in check:
        if c > 1:
            cnt += 1
    if cnt >= 2:
        result.append(i)
        continue
# 6. 최근 7번에서 3번 이상 등장했던 숫자 쌍이 2개 이상인 경우는 없다.
    past = a[i-7:i]
    check = [0 for _ in range(46)]
    for x in past:
        for y in current:
            if y in x:
                check[y] += 1
    cnt = 0
    for c in check:
        if c > 2:
            cnt += 1
    if cnt >= 2:
        result.append(i)
        continue
# 7. 최근 10번에서 3번 이상 등장했던 숫자 쌍이 3개 이상인 경우는 없다.
    past = a[i-10:i]
    check = [0 for _ in range(46)]
    for x in past:
        for y in current:
            if y in x:
                check[y] += 1
    cnt = 0
    for c in check:
        if c >= 3:
            cnt += 1
    if cnt >= 3:
        result.append(i)
        continue

# 8. 최근 15번에서 4번 이상 등장했던 숫자 쌍이 3개 이상인 경우는 없다.
    past = a[i-15:i]
    check = [0 for _ in range(46)]
    for x in past:
        for y in current:
            if y in x:
                check[y] += 1
    cnt = 0
    for c in check:
        if c >= 4:
            cnt += 1
    if cnt >= 3:
        result.append(i)
        continue

# 9. 최근 120개에서 3개이상 겹치는 경우가 있다.
    past = a[i-120:i]
    r = 0
    for x in past:
        cnt = 0
        for y in current:
            if y in x:
                cnt += 1
        if cnt >= 3:
            r = 1
            break
    if r == 0:
        result.append(i)

# 10. 최근 25개에서 2개이상 겹치는 경우가 무조건 있다.
    past = a[i-25:i]
    r = 0
    for x in past:
        cnt = 0
        for y in current:
            if y in x:
                cnt += 1
        if cnt > 1:
            r = 1
            break
    if r == 0:
        result.append(i)

print(result)
print(len(result))
