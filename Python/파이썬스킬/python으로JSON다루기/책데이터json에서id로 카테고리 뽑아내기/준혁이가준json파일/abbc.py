import json
# 총 데이터의 갯수는 28243개
with open('bookdata.json', encoding='utf-16') as json_file:
    json_data = json.load(json_file)
    print(len(json_data))



with open('abcd.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")