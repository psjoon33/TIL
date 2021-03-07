import sys
sys.stdin = open('식품대분류.txt', 'r', encoding='UTF8')

cates = []
for i in range(42424):
    n = input()
    if n not in cates:
        cates.append(n)
# print(cates)
# print(len(cates))
for i in cates:
    print(i)
# 총 174개의 대분류가 존재