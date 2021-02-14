import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    represent = {}

    arr = []
    idx = []
    for i in range(len(json_data)):
        if '가공유' in json_data[i]['분류']:
            if '라떼' in json_data[i]['식품명']:
                arr.append(json_data[i])
                idx.append(i)
    cnt = len(arr)

    represent['식품명'] = '라떼'
    represent['분류'] = '가공유'
    # 위에 내가 설정
    represent['1회제공량'] = '200'
    represent['단위'] = 'ml'
    # 여기 위에도 내가 설정

    standard = ['에너지', '단백질', '지방', '탄수화물', '총당류', '나트륨', '콜레스테롤(g)', 
    '콜레스테롤(mg)', '총포화지방산', '트랜스지방산'
    ]
    for s in standard:
        represent[s] = 0
    # print(represent)

    for a in arr:
        di = a['1회제공량']
        for s in standard:
            represent[s] += float(a[s])/float(a['1회제공량'])

    for  x in standard:
        represent[x] = str(round(represent[x] * int(represent['1회제공량']) / cnt, 2))

    print(represent)
    json_data.insert(idx[0], represent)

with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")
