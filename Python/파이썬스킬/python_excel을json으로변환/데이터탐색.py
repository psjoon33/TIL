import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    idx = []
    for i in range(len(json_data)):
        if '과/채음료' == json_data[i]['분류']:                    
            # if '당면' not in json_data[i]['식품명']:
            idx = [i] + idx
            print(i, end=' ')
            print(json_data[i]['식품명'])
    print(idx)
    print(len(idx))
    
    # print(json_data[185])
    # json_data.pop(184)    
    # json_data[251]['식품명'] = '백도'
    # json_data[238]['식품명'] = '튀김가루'
    # json_data[244]['식품명'] = '백설 빵가루'
    # json_data[2]['식품명'] = '립톤 아이스티믹스 레몬맛'
    # json_data[188], json_data[197] = json_data[197], json_data[188]
    
    # for i in idx:
    #     json_data.pop(i)

# with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
#     json.dump(json_data, make_file, ensure_ascii=False, indent="\t")



