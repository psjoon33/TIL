import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    
    for i in range(len(json_data)):
        json_data[i]['제공량'] = json_data[i].pop('1회제공량')

    
    
    # print(idx)
    # print(len(idx))


with open('newInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")


