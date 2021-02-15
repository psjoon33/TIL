cates = ['포도', '레몬', '석류', '깔라만시', '오렌지', '파인애플', '사과', '노니', '매실', '양배추', '호박', '감귤', '망고', '당근', '블루베리', '양파', '자몽',
'토마토', '야채', '오디', '마늘', '바나나', '한라봉', '복숭아', '배', 
'아로니아', '도라지', '키위', '알로에', '복분자', '유자', '딸기']

import json


with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    
    idx = []
    l = len(json_data)
    for i in range(l):
        if json_data[i]['분류'] == '과/채음료':
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




