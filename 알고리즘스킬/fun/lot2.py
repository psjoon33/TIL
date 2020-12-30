import sys
sys.stdin = open('로또.txt', 'r')
a = []
for i in range(942):
    a.append(list(map(int, input().split('\t'))))

result = 0
for i in range(917):
    x = a[i]








