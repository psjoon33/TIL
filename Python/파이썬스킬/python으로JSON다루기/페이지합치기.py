import requests
from kobis import URLMaker
import json

def filmo_count(page):
    url_maker = URLMaker('c94ff0a895a99423430945754296e797')
    url = url_maker.get_url()
    payload = f'page={page}'
    # URL 요청
    r = requests.get(url,params = payload)
    # json파일을 해석하여 str 타입을 dic타입으로 변환
    people_dict = r.json()
    # 주소에서 'peopleListResult'안에 'peopleList'로 접근
    return people_dict


file_data = []
x = []
y = []
z = []
for i in range(1, 20):
    file_data.extend(filmo_count(i)['results'])
    for j in range(((i-1)*20), 20*i):
        a = file_data[j]['release_date'][0:4]
        if int(a) >= 2016:
            x.append(file_data[j])
        elif 2011 <= int(a) < 2016:
            y.append(file_data[j])
        elif 2007 <= int(a) < 2011:
            z.append(file_data[j])


actions = x + y + z
actions = actions[4:]
# print(actions)  
for i in range(len(actions)):
    actions[i]['poster_path'] = 'https://image.tmdb.org/t/p/w500' + actions[i]['poster_path']
    actions[i]['idx'] = i
    


with open('movies1.json', 'w', encoding='utf-8') as make_file:
    json.dump(actions, make_file, ensure_ascii=False, indent="\t")



# results = []
# for x in actions:
#     if 10752 in x['genre_ids']:
#         results.append(x)

# with open('wars.json', 'w', encoding='utf-8') as make_file:
#     json.dump(results, make_file, ensure_ascii=False, indent="\t")