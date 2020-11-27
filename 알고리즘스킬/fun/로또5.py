import sys
sys.stdin = open('로또.txt', 'r')

result = []
for i in range(10):
    result.append(list(map(int, input().split('\t'))))
# print(result)

def lotto(nums):
    res = 'Yes'
    for x in result:
        cnt = 0
        for y in nums:
            if y in x:
                cnt += 1

        if cnt >= 2:
            res = 'No' + '/ index: ' + str(result.index(x))
            break
    return res

print(lotto([5, 19, 17, 20, 25, 34]))