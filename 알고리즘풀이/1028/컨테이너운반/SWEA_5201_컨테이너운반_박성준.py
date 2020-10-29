import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    goods = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    result = 0
    while True:
        if trucks[0] >= goods[0]:
            result += goods.pop(0)
            trucks.pop(0)
        elif trucks[0] < goods[0]:
            goods.pop(0)
        
        if len(trucks) == 0 or len(goods) == 0:
            break

    print('#{} {}'.format(tc, result))


