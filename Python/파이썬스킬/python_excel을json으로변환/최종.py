import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    
    # 데이터의 총 갯수는 23794개

    names = []

    out = []

    idx = []
    for i in range(len(json_data)):
    # for i in range(len(json_data)-1, -1, -1):
        n = json_data[i]['분류']
        if n not in names:
            names.append(n)
        # else:
        #     out.append(n)
        #     idx.append(i)
    # print(idx)
    
    # print(len(out))
    # print(out)
    print(len(names))
    print(names)