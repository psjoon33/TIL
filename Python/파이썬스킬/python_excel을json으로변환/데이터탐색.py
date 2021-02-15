import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    idx = []
    for i in range(len(json_data)):
        if '과/채주스' == json_data[i]['분류']:                    
            # if '딸기' in json_data[i]['식품명']:
            idx = [i] + idx
            print(i, end=' ')
            print(json_data[i]['식품명'])
    print(idx)
    print(len(idx))
    
    # print(json_data[185])
    # json_data.pop(371)    
    # json_data[333]['식품명'] = '꿀유자'
    # json_data.pop(350)
    # json_data.pop(5)
    # json_data[312]['식품명'] = '배즙'
    # json_data[590]['식품명'] = '남양 at home 제주감귤'
    
    # for i in idx:
    #     json_data.pop(i)

# with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
#     json.dump(json_data, make_file, ensure_ascii=False, indent="\t")



