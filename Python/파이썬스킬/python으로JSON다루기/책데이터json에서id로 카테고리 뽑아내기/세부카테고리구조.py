import sys
import json

with open('key-category.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # 전체 카테고리의 갯수는 10180
    sub_category = {'국내도서':{}, '외국도서':{}}

    for num in json_data:
        if len(json_data[num]) == 1:
            continue
        elif len(json_data[num]) == 2:
            if json_data[num][0] == '국내도서':
                if json_data[num][1] not in sub_category['국내도서']:
                    sub_category['국내도서'][json_data[num][1]] = []
                else:
                    continue
            else:
                if json_data[num][1] not in sub_category['외국도서']:
                    sub_category['외국도서'][json_data[num][1]] = []
                else:
                    continue

        else:
            if json_data[num][0] =='국내도서':
                if json_data[num][1] not in sub_category['국내도서']:
                    sub_category['국내도서'][json_data[num][1]] = [json_data[num][2]]
                else:
                    if json_data[num][2] not in sub_category['국내도서'][json_data[num][1]]:
                        sub_category['국내도서'][json_data[num][1]].append(json_data[num][2])
            else:
                if json_data[num][1] not in sub_category['외국도서']:
                    sub_category['외국도서'][json_data[num][1]] = [json_data[num][2]]
                else:
                    if json_data[num][2] not in sub_category['외국도서'][json_data[num][1]]:
                        sub_category['외국도서'][json_data[num][1]].append(json_data[num][2])
                
    print(sub_category)
    
with open('category-structure.json', 'w', encoding='utf-8') as make_file:
    json.dump(sub_category, make_file, ensure_ascii=False, indent="\t")



