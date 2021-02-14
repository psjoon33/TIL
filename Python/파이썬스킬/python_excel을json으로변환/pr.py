import sys
sys.stdin = open('r.txt', 'r', encoding='UTF8')

l = []
for i in range(2):
    l.append(list(map(str, input().split('\t'))))

print(l)
