# 최근 200개에 4개 이상 있는지 고려

import sys
sys.stdin = open('로또.txt', 'r')

result = []
for i in range(200):
    result.append(list(map(int, input().split('\t'))))
def lotto(nums):
    res = 'Yes'
    for x in result:
        cnt = 0
        for y in nums:
            if y in x:
                cnt += 1
        if cnt >= 4:
            res = 'No' + '/ index: ' + str(result.index(x))
            print(x)
            break
    return res

print(lotto([5, 8, 11, 12, 24, 30]))