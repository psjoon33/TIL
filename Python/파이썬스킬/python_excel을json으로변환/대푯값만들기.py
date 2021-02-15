import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    represent = {}

    arr = []
    idx = []
    for i in range(len(json_data)):
        if '고추장' in json_data[i]['분류']:
            # if '당면' in json_data[i]['식품명']:
            arr.append(json_data[i])
            idx.append(i)
    cnt = len(arr)

    represent['식품명'] = '고추장'
    represent['분류'] = '고추장'
    # 위에 내가 설정
    represent['1회제공량'] = '100'
    represent['단위'] = 'g'
    # 여기 위에도 내가 설정

    standard = ['에너지', '단백질', '지방', '탄수화물', '총당류', '나트륨', '콜레스테롤(g)', 
    '콜레스테롤(mg)', '총포화지방산', '트랜스지방산'
    ]
    for s in standard:
        represent[s] = 0
    print(represent)

    for a in arr:
        for s in standard:
            represent[s] += float(a[s])/float(a['1회제공량'])

    for  x in standard:
        represent[x] = str(round(represent[x] * int(represent['1회제공량']) / cnt, 2))

    print(represent)
    represent['1회제공량'] = str(10)
    represent['에너지'] = str(1.9)
    represent['탄수화물'] = str(0.34)
    represent['단백질'] =str(0.05)
    represent['지방'] = str(0.02)
    represent['총당류'] = str(0.23)
    represent['나트륨'] = str(20.82)
    represent['총포화지방산'] = str(0.0)
    print(represent)
    json_data.insert(idx[0], represent)

with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")
