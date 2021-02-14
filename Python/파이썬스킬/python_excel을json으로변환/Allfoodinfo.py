import json
import sys
sys.stdin = open('r.txt', 'r', encoding='UTF8')


result = []
for i in range(46894):
    a = list(map(str, input().split('\t')))
    if len(a) != 14:
        print(i)
        print(a)
        continue
    # print(a)
    r = {}

    r['식품명'] = a.pop(0)
    r['분류'] = a.pop(0)
    r['1회제공량'] = a.pop(0)
    r['단위'] = a.pop(0)
    r['에너지'] = a.pop(0)
    r['단백질'] = a.pop(0)
    r['지방'] = a.pop(0)
    r['탄수화물'] = a.pop(0)
    r['총당류'] = a.pop(0)
    r['나트륨'] = a.pop(0)
    r['콜레스테롤(g)'] = a.pop(0)
    r['콜레스테롤(mg)'] = a.pop(0)
    r['총포화지방산'] = a.pop(0)
    r['트랜스지방산'] = a.pop(0)
    result.append(r)

# print(len(result))
# print(result)
with open('foodInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")