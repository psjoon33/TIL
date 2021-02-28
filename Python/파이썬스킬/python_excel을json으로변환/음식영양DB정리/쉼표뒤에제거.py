import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    idx = []    
    for i in range(len(json_data)):
        if '채소류' == json_data[i]['분류']:
            # print(json_data[i]['식품명'])
            for x in range(len(json_data[i]['식품명'])):
                if json_data[i]['식품명'][x] == ',':
                    json_data[i]['식품명'] = json_data[i]['식품명'][0:x]
                    break
            # print(json_data[i]['식품명'])
            
with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")
