cates = ['남양', '비피더스', '파스퇴르', '요플레', '빙그레']

import json


with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    
    idx = []
    l = len(json_data)
    for i in range(l):
        if json_data[i]['분류'] == '발효유':
            result = 'out'
            name = json_data[i]['식품명']
            for c in cates:
                if c in name:
                    result = 'pass'
                    break
            if result == 'out':
                idx = [i] + idx
    print(idx)
    for i in idx:
        print(i, end=' ')
        print(json_data[i]['식품명'])




