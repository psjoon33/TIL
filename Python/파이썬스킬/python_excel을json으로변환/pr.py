import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

a = list(map(str, input().split(', ')))

print(a)


for i in range(10, -1, -1):
    print(i)