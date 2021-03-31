import sys
import json

with open('category-structure.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    domestic = json_data['국내도서']
    
    result ={'국내도서':[], '외국도서':[]}
    for x in domestic:
        if len(domestic[x]) == 0:
            continue
        result['국내도서'].append(x)
    
    foreign = json_data['외국도서']
    for x in foreign:
        if len(foreign[x]) == 0:
            continue
        result['외국도서'].append(x)

with open('secondcategory.json', 'w', encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")