import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    idx = [
        ]
    for i in idx:
        json_data.pop(i)

    # json_data[114]['분류'] = '가공유'
    # json_data[115]['분류'] = '가공유'



with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

