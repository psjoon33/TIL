import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    idx = []
    print(json_data[68])
    print(json_data[72])
    nameset = []
    for i in range(len(json_data)):
        if json_data[i]['식품명'] not in nameset:
            nameset.append(json_data[i]['식품명'])
        else:
            idx = [i] + idx
            # print(i, end=' ')
            # print(json_data[i]['식품명'])
    # print(nameset)
    # print(idx)
    # print(len(idx))


# with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
#     json.dump(json_data, make_file, ensure_ascii=False, indent="\t")


