from operator import itemgetter
import re
import json
# 총 데이터의 갯수는 28243개
with open('bookdata.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    result=[]
    for x in json_data:
        if x['country'] == '국내도서':
            if x['subcategory'] == '액션/스릴러소설':
                result.append(x)
        if len(result) == 30:
            break

    for r in result:
        print(r['title'])

    # find = ['경제적 해자 - 부자를 만드는 주식투자의 공식', '좋은 주식 나쁜 주식 - 부의 추월차선에 오르기 위한 진짜 주식 공부', '부자의 역사 - 부자의 탄생과 몰락에서 배우는 투자 전략', '경제용어도감', '주린이가 가장 알고 싶은 최다질문 TOP 77']
    # new_result = []
    # for r in result:
    #     if r['title'] in find:
    #         new_result.append(r)


with open('액션스릴러소설.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")