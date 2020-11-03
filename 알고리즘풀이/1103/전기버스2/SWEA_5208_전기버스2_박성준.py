import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    N = nums.pop(0)

    loc = 1
    cnt = 0
    while True:
        length = nums.pop(0)
        
        if length + loc >= N:
            break
        
        M = 0
        for i in range(length):
            if M < i + nums[i]:
                M = i + nums[i]
                Mi = i

        nums = nums[Mi:]
        cnt += 1
        loc = loc + 1 + Mi

    print('#{} {}'.format(tc, cnt))










