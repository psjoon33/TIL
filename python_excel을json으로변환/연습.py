import sys
sys.stdin = open('r.txt', 'r', encoding='UTF8')

l = []
for i in range(4):
    l.append(list(map(str, input().split('\t'))))

print(l)




# print(df_excel)

