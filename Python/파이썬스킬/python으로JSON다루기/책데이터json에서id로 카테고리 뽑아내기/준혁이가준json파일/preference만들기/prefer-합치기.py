from operator import itemgetter
import re
import json
# 총 데이터의 갯수는 28243개
with open('한국소설.json', encoding='utf-8') as json_file:
    json_data1 = json.load(json_file)
with open('판타지소설.json', encoding='utf-8') as json_file:
    json_data2 = json.load(json_file)
with open('추리-미스터리소설.json', encoding='utf-8') as json_file:
    json_data3 = json.load(json_file)
with open('경제경영.json', encoding='utf-8') as json_file:
    json_data4 = json.load(json_file)
with open('일본소설.json', encoding='utf-8') as json_file:
    json_data5 = json.load(json_file)
with open('자기계발.json', encoding='utf-8') as json_file:
    json_data6 = json.load(json_file)
with open('과학소설(SF).json', encoding='utf-8') as json_file:
    json_data7 = json.load(json_file)
with open('로맨스소설.json', encoding='utf-8') as json_file:
    json_data8 = json.load(json_file)



result = []
for i in range(5):
    json_data1[i]['preference-category'] = '한국소설'
    json_data2[i]['preference-category'] = '판타지소설'
    json_data3[i]['preference-category'] = '추리/미스터리소설'
    json_data4[i]['preference-category'] = '경제경영'
    json_data5[i]['preference-category'] = '일본소설'
    json_data6[i]['preference-category'] = '자기계발'
    json_data7[i]['preference-category'] = '과학소설(SF)'
    json_data8[i]['preference-category'] = '로맨스소설'
    result.append(json_data1[i])
    result.append(json_data2[i])
    result.append(json_data3[i])
    result.append(json_data4[i])
    result.append(json_data5[i])
    result.append(json_data6[i])
    result.append(json_data7[i])
    result.append(json_data8[i])


print(len(result))

with open('preference.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")