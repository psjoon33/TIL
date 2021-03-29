import json

with open('book_domestic.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

with open('bookdatas.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")