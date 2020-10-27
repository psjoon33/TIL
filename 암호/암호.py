import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())

# 16진법에서 2진법으로 바꿔주는 함수
def StoB(x):
    y = int(x, 16)
    z = ''
    for i in range(4):
        z = str(y % 2) + z
        y = y // 2
    return z

decode =[[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

for tc in range(1, T+1):
    r, c = map(int, input().split())
    numbers = []
    for _ in range(r):
        n = input()
        if n != '0'*c and n not in numbers:
            numbers.append(n)
    # print('#{} {}'.format(tc, numbers))

    arr = []
    for number in numbers:
        res = ''
        for n in number:
            res = res + StoB(n)
        arr.append(res)
    # print(arr)

    result = 0
    for a in arr:
        while True:
            b = a.find('1')
            # print(b)
            x, y, z = 0, 0, 0
            # 1의갯수
            while a[b] == '1':
                x += 1
                b += 1
            while a[b] == '0':
                y += 1
                b += 1
            while a[b] == '1':
                z += 1
                b += 1
            
            l = 0
            gop = 1
            while True:
                for i in range(10):
                    if x == decode[i][1]*gop and y == decode[i][2]*gop and z == decode[i][3]*gop:
                        l = gop
                        break
                if l != 0:
                    break
                else:
                    gop += 1
            # print('#{} {}'.format(tc, gop))
            # 곱을 찾았다. 
            # print(gop)
            # print(i)

            # 시작인덱스를 찾자...
            # 일단 시작 1의 인덱스는 b
            
            start = a.find('1') - (decode[i][0] * gop)
            # print(start)
            need = a[start:start + 56 *gop]
            # print(need)
            
            # 1개당 길이 
            length = 7 * gop

            g = gop
            subs = ['000'*g + '11'*g + '0'*g + '1'*g, '00'*g+'11'*g+'00'*g+'1'*g, '00'*g+'1'*g+'00'*g+'11'*g, '0'*g + '1111'*g + '0'*g + '1'*g, '0'*g + '1'*g + '000'*g + '11'*g, '0'*g + '11'*g + '000'*g + '1'*g, '0'*g + '1'*g + '0'*g + '1111'*g, '0'*g + '111'*g+ '0'*g + '11'*g, '0'*g + '11'*g + '0'*g + '111'*g, '000'*g + '1'*g + '0'*g +'11'*g]
            # print(subs)
            res = []
            for x in range(8):
                s = subs.index(need[7*x*gop:(7*x+7)*gop])
                res.append(s)

            tot = sum(res) + res[0]*2 + res[2]*2 + res[4]*2 + res[6]*2
            if tot % 10 == 0:
                result += sum(res)
        
            a = a[start + 56*gop:]
            if a == '0'*len(a):
                break
    print('#{} {}'.format(tc, result))










