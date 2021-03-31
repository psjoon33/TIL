import sys
import json
sys.stdin = open('카테고리데이터.txt', 'r', encoding='utf-8')
n = 10755

cates = {}

for i in range(n):
    cate = list(map(str, input().split('\t')))
    if cate[2] != '국내도서' and cate[2] != '외국도서':
        continue
    detail = [cate[2]]
    
    for i in range(3, 5):
        if cate[i] != '':
            detail.append(cate[i])
        else:
            break
    cates[cate[0]] = detail

print(cates)

with open('key-category.json', 'w', encoding='utf-8') as make_file:
    json.dump(cates, make_file, ensure_ascii=False, indent="\t")