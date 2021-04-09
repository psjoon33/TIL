from operator import itemgetter
import re
import json
with open('sliced-bookdata.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # for i in range(len(json_data)):
    # json_data[i]['sliced_title'] = json_data

    for i in range(len(json_data)):
        if len(json_data[i]['title']) > 60 :
            json_data[i]['sliced_title'] = json_data[i]['title'][0:60] + '....'
        else:
            json_data[i]['sliced_title'] = json_data[i]['title']

with open('bookdata.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")