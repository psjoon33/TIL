from operator import itemgetter
import re
import json
# 총 데이터의 갯수는 28243개
with open('all.json', encoding='utf-16') as json_file:
    json_data = json.load(json_file)
    for i in range(len(json_data)):
        y = json_data[i]['title']
        z = json_data[i]['book_summary']
        
        if '&lt;' in y:
            y = re.sub('&lt;', '[', y)
            y = re.sub('&gt;', ']', y)
        if json_data[i]['book_summary'] is not None and json_data[i]['book_summary'] != '':
            if '&lt;' in z:
                z = re.sub('&lt;', '[', z)
                z = re.sub('&gt;', ']', z)
                print(z)
        json_data[i]['title'] = y
        json_data[i]['book_summary'] = z



with open('alldata.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")