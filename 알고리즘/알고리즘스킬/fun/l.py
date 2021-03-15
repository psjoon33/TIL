import sys
sys.stdin = open('l.txt', 'r')
a = []
for i in range(953):
    # a.append(list(map(int, input().split('\t'))))
    a = [list(map(int, input().split('\t')))] + a

result = 0
for i in range(800, 953):
    x = a[i]
    y = a[i-800:i]
    for z in y:
        cnt = 0
        for w in x:
            if w in z:
                cnt += 1
        if cnt >= 4:
            result += 1
            break
print(result)