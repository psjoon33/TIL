import json
# 총 데이터의 갯수는 28243개
with open('sliced-bookdata.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    structure = {'국내도서':{}, '외국도서':{}}
    for x in json_data:
        if x['country'] == '국내도서':
            if x['maincategory'] not in structure['국내도서']:
                structure['국내도서'][x['maincategory']] = []
            if x['subcategory'] not in structure['국내도서'][x['maincategory']]:
                structure['국내도서'][x['maincategory']].append(x['subcategory'])
        elif x['country'] == '외국도서':
            if x['maincategory'] not in structure['외국도서']:
                structure['외국도서'][x['maincategory']] = []
            if x['subcategory'] not in structure['외국도서'][x['maincategory']]:
                structure['외국도서'][x['maincategory']].append(x['subcategory'])



with open('categorystructure2.json', 'w', encoding='utf-8') as make_file:
    json.dump(structure, make_file, ensure_ascii=False, indent="\t")