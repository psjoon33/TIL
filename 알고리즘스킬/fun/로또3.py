# 최근 100개에 4개 이상 있는지 고려

import sys
sys.stdin = open('로또.txt', 'r')

result = []
for i in range(150):
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

print(lotto([3, 15, 20, 22, 24, 41]))