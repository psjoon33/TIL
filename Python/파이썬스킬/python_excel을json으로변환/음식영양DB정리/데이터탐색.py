import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    idx = []    
    for i in range(len(json_data)):
        if '육류' == json_data[i]['분류']:
            # if 'I' in json_data[i]['식품명']:   
            idx = [i] + idx
            print(i, end=' ')
            print(json_data[i]['식품명'])
    print(idx)
    print(len(idx))

    # print(json_data[14470])
    # print(json_data[185])
    # json_data.pop(17376)   

    json_data[15738]['식품명'] = '소 꽃갈비'
    json_data[15739]['식품명'] = '소 갈비'
    json_data[15740]['식품명'] = '소 안창살'
    json_data[15741]['식품명'] = '소 제비추리'
    json_data[15742]['식품명'] = '소 참갈비'
    json_data[15743]['식품명'] = '소 토시살'
    json_data[15744]['식품명'] = '소 꽃등심살'
    json_data[15745]['식품명'] = '소 살치살'
    json_data[15746]['식품명'] = '소 아래등심살'
    json_data[15747]['식품명'] = '소 윗등심살'
    json_data[15748]['식품명'] = '소 목심살'
    json_data[15749]['식품명'] = '소 뒷사태'
    json_data[15750]['식품명'] = '소 뭉치사태'
    json_data[15751]['식품명'] = '소 상박살'
    json_data[15752]['식품명'] = '소 아롱사태'
    json_data[15753]['식품명'] = '소 앞사태'
    json_data[15754]['식품명'] = '소고기'
    json_data[15755]['식품명'] = '소 도가니살'
    json_data[15756]['식품명'] = '소 보섭살'
    json_data[15757]['식품명'] = '소 삼각살'
    json_data[15758]['식품명'] = '소 설깃머리살'
    json_data[15759]['식품명'] = '소 설깃살'
    json_data[15760]['식품명'] = '소 안심'
    json_data[15761]['식품명'] = '소 갈비덧살'
    json_data[15762]['식품명'] = '소 꾸리살'
    json_data[15763]['식품명'] = '소 부채덮개살'
    json_data[15764]['식품명'] = '소 부채살'
    json_data[15765]['식품명'] = '소 앞다리살'
    json_data[15766]['식품명'] = '소 앞치마살'
    json_data[15767]['식품명'] = '소 양지'
    json_data[15768]['식품명'] = '소 업진살'
    json_data[15769]['식품명'] = '소 업진안살'
    json_data[15770]['식품명'] = '소 차돌박이'
    json_data[15771]['식품명'] = '소 치마살'
    json_data[15772]['식품명'] = '소 치마양지'
    json_data[15773]['식품명'] = '소 우둔살'
    json_data[15774]['식품명'] = '소 홍두깨살'
    json_data[15775]['식품명'] = '소 채끝살'

    # json_data[15738]['식품명'] = ''
    # json_data[15739]['식품명'] = ''
    # json_data[15740]['식품명'] = ''

    # json_data[1569]['식품명'] = ''

    # for i in idx:
    #     json_data.pop(i)

# with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
#     json.dump(json_data, make_file, ensure_ascii=False, indent="\t")



