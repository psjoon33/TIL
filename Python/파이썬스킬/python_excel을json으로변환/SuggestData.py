import json
import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
nominee = list(map(str, input().split(', ')))

with open('newInfo.json', encoding='utf-8') as json_file:
	json_data = json.load(json_file)
with open('suggestInfo.json', encoding='utf-8') as json_file:
	suggestInfo = json.load(json_file)
with open('추천음식리스트.json', encoding='utf-8') as json_file:
	suggest = json.load(json_file)	

	for n in nominee:
		result = 'no'
		for i in range(len(json_data)):
			if n == json_data[i]['식품명']:
				if n not in suggest:
					print('{}는 있어요'.format(n))
					print()
					result = 'yes'
					suggest.append(n)
					suggestInfo.append(json_data[i])
					break
				else:
					print('{}는 이미 들어가있어요'.format(n))
					result = 'yes'

		if result == 'no':
			print('{}는 데이터가 없어요'.format(n))
			print()






with open('suggestInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(suggestInfo, make_file, ensure_ascii=False, indent="\t")

with open('추천음식리스트.json', 'w', encoding='utf-8') as make_file:
    json.dump(suggest, make_file, ensure_ascii=False, indent="\t")

