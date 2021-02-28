import sys
import json

with open('고기구이싫어.json', encoding='utf-8') as json_file:
	nosnack = json.load(json_file)
no = {}
no['nosnack'] = nosnack
    




with open('통합본.json', 'w', encoding='utf-8') as make_file:
    json.dump(no, make_file, ensure_ascii=False, indent="\t")