#  1등 당첨번호 6개만 고려.
#  4등 맞는게 3개 이하

import sys
sys.stdin = open('로또.txt', 'r')

result = []
for i in range(937):
    result.append(list(map(int, input().split('\t'))))

def lotto(nums):
    rate = {'3':0, '4':0, '5':0, '6':0}
    for x in result:
        cnt = 0
        for y in nums:
            if y in x:
                cnt += 1
        if cnt >= 4:
            print('#{} idx:{} 갯수:{}'.format(x, result.index(x), cnt))
        cnt = str(cnt)
        
        if cnt in rate:
            rate[cnt] += 1
    return rate

print(lotto([1, 2, 5, 24, 26, 44]))