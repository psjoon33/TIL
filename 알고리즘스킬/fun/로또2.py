# 2등 당첨번호까지 더해서 7개 중
# 몇 개가 맞았는지 고려.

import sys
sys.stdin = open('로또2.txt', 'r')

result = []
for i in range(938):
    result.append(list(map(int, input().split('\t'))))
def lotto(nums):
    rate = {'3':0, '4':0, '5':0, '6':0}
    global el

    el = 0
    for x in result:
        cnt = 0
        for y in nums:
            if y in x:
                cnt += 1
        if cnt >= 4:
            print('#{} index:{} 갯수:{}'.format(x, result.index(x), cnt))
        cnt = str(cnt)
        
        if cnt in rate:
            rate[cnt] += 1
        else:
            el += 1
    return rate

print(lotto([3, 15, 20, 22, 24, 41]))
