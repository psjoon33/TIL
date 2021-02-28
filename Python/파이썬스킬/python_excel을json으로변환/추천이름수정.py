import json

with open('suggestInfo.json', encoding='utf-8') as json_file:
	suggestInfo = json.load(json_file)
with open('추천음식리스트.json', encoding='utf-8') as json_file:
	suggest = json.load(json_file)	

old = '닭발구이'
new = '닭발'

for i in range(100):
    if suggest[i] == old:
        suggest[i] = new
        print('수정완료!')
        break

for i in range(100):
    if suggestInfo[i]['식품명'] == old:
        suggestInfo[i]['식품명'] = new
        break


with open('suggestInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(suggestInfo, make_file, ensure_ascii=False, indent="\t")

with open('추천음식리스트.json', 'w', encoding='utf-8') as make_file:
    json.dump(suggest, make_file, ensure_ascii=False, indent="\t")



