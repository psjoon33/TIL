import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    number, N = map(str, input().split())
    N = int(N)
    number = [int(n) for n in number]
    # print(number)

    goal = sorted(number, reverse = True)
    # print(goal)
    # print(number)

    cnt = 0
    while True:
        # print('#{} {}'.format(cnt, number))
        if goal == number:
            r = 0
            for x in goal:
                # print(1)
                if goal.count(x) > 1:
                    result = number
                    # print(result)
                    r = 1
                    break
            if r == 1:
                res = ''
                for i in result:
                    res += str(i)

                print('#{} {}'.format(tc, res))
                break

            # r != 1 이라는 것은, 중복되는 수가 없다는 뜻...
            else:
                # print(2)
                if (N - cnt) % 2 == 1:
                    number[len(number)-2], number[len(number)-1] = number[len(number)-1], number[len(number)-2]
                    result = number
                else:
                    result = number

                # print(result)
                res = ''
                for i in result:
                    res += str(i)
                print('#{} {}'.format(tc, res))
                break
        
        else:
            x = 0
            while True:
                
                if goal[x] == number[x]:
                    x += 1
                    continue
                else:
                    sli = number[x:]
                    MA = max(sli)
                    CMA = sli.count(MA)
                    if CMA >= len(sli) - CMA and N - cnt >= len(sli) - CMA:
                        number = goal

                    z = number[x:]
                    y = max(z)
                    w = list(reversed(z))
                    # print(w)
                    # print(z)
                    a = w.index(y)
                    # number에서 바꿔야 하는 인덱스: x랑 len(number) -1 - a
                    number[x], number[len(number) - 1 - a] = number[len(number) - 1 - a], number[x]
                    cnt += 1
                    # print(number)
                    break

        if cnt == N:
            res = ''
            for i in number:
                res += str(i)
            print('#{} {}'.format(tc, res))
            break


