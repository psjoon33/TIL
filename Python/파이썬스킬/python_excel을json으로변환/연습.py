import json

with open('suggestInfo.json', encoding='utf-8') as json_file:
	suggestInfo = json.load(json_file)
with open('추천음식리스트.json', encoding='utf-8') as json_file:
	suggest = json.load(json_file)	

print(len(suggestInfo))