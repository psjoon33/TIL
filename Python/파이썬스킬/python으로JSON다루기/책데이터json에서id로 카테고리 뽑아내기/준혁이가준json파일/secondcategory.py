import json
# 총 데이터의 갯수는 28243개
with open('categorystructure2.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    domestic = json_data['국내도서']
    result = {'국내도서':[], '외국도서':[]}
    for x in domestic:
        result['국내도서'].append(x)
    foreign = json_data['외국도서']
    for x in foreign:
        result['외국도서'].append(x)
    # print(result)

with open('second-category2.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")

