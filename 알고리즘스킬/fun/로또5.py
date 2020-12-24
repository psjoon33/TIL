import sys
sys.stdin = open('로또.txt', 'r')
# 최근 10 번 중에 2개이상 같은 수가 겹치는 지를 확인
result = []
for i in range(10):
    result.append(list(map(int, input().split('\t'))))
def lotto(nums):
    res = 'Yes'
    for x in result:
        cnt = 0
        for y in nums:
            if y in x:
                cnt += 1
        if cnt >= 2:
            print('No' + '/ index: ' + str(result.index(x)))
            print(x)
            res = 0
            break
    if res != 0:
        print(res)
    return

lotto([5, 8, 11, 16, 24, 29])