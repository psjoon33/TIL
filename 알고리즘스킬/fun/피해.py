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
        if cnt == 5:
            print('#{} 얘의idx:{} 갯수:{} 나:{} 나의idx:{}'.format(x, result.index(x), cnt, nums, result.index(nums)))
        cnt = str(cnt)
        
        if cnt in rate:
            rate[cnt] += 1
    return rate

c = 0
for k in result:
    l = lotto(k)
    if l['5'] > 0:   
        c += 1
print(c)