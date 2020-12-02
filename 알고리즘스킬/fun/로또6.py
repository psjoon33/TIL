# 최근 5번 중 2번 이상 들어간 수가 2개 이상 들어간 경우 'NO'
import sys
sys.stdin = open('로또.txt', 'r')
result = []
for i in range(5):
    result.append(list(map(int, input().split('\t'))))
def lotto(nums):
    res = 'Yes'
    check = 0
    for x in nums:
        cnt = 0
        for y in result:
            if x in y:
                cnt += 1
        if cnt >= 2:
            check += 1

    if check >= 2:
        res = 'No'
    return res

print(lotto([3, 9, 10, 34, 35, 41]))