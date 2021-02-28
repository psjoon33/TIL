import json
import sys
with open('추천음식리스트.json', encoding='utf-8') as json_file:
	suggest = json.load(json_file)

sys.stdin = open('input.txt', 'r', encoding='utf-8')
nofoods = list(map(str, input().split(', ')))
nofoods.reverse()
print(nofoods)


# new = []
# keyword = '밥'
# for s in suggest:
#     for nofoods in 
#         new.append(s)
# new.reverse()
# print(new)

with open('새싫어.json', 'w', encoding='utf-8') as make_file:
    json.dump(nofoods, make_file, ensure_ascii=False, indent="\t")