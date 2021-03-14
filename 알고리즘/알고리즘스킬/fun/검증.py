import sys
sys.stdin = open('l.txt', 'r')

a = []
n = 953
# n은 몇 회차인지

for i in range(n):
    # a.append(list(map(int, input().split('\t'))))
    a = [list(map(int, input().split('\t')))] + a
print(len(a))
# 룰에 어긋나는 경우의 카운트를 result
result = []

# 1. 같은 수가 4번 연속 나오는 경우는 없다. 
for i in range(120, n):
    current = a[i]
#     past = a[i-3:i]
#     for x in current:
#         if x in past[0] and x in past[1] and x in past[2]:
#             result.append(i)
#             continue

# 2. 이전 회차와 3개 이상 겹치는 경우는 없다.
    # past = a[i-1]
    # cnt = 0
    # for x in current:
    #     if x in past:
    #         cnt += 1
    # if cnt >= 3:
    #     result.append(i)
    #     continue

# 3. 56개를 봤을 때 4개 이상 겹치는 경우는 없다.
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
            
        
print(result)
print(len(result))
