import sys
sys.stdin = open('식품상세분류.txt', 'r', encoding='UTF8')

cates = []
for i in range(42424):
    n = input()
    if n not in cates:
        cates.append(n)
print(cates)
print(len(cates))

# 총 275개의 상세분류가 존재