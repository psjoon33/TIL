import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    idx = []
    for i in range(len(json_data)):
        if '가공치즈' == json_data[i]['분류']:
            if '체다' in json_data[i]['식품명']:
                idx += [i] + idx
                print(i, end=' ')
                print(json_data[i]['식품명'])
            
    print(idx)
    print(len(idx))


# with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
#     json.dump(json_data, make_file, ensure_ascii=False, indent="\t")



