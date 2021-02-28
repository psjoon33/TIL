import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    names = []
    idx = []
    for i in range(len(json_data)):
        if '캔디류' == json_data[i]['분류']:
            if json_data[i]['식품명'] not in names:
                names.append(json_data[i]['식품명'])
            else:
                # print(json_data[i])
                idx = [i] + idx
    print(idx)
    # print(names)

