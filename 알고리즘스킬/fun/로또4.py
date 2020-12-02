# 최근 20개에 3개 이상 있는지 고려

import sys
sys.stdin = open('로또.txt', 'r')
result = []
for i in range(40):
    result.append(list(map(int, input().split('\t'))))
def lotto(nums):
    res = 'Yes'
    for x in result:
        cnt = 0
        for y in nums:
            if y in x:
                cnt += 1
        if cnt >= 3:
            print(x)
            res = 'No' + '/ index: ' + str(result.index(x))
            break
    return res

print(lotto([3, 9, 10, 34, 35, 41]))