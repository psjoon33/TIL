import json

with open('movies.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    
# print(json_data[0])

new = []
for movie in json_data:
    if 10752 in movie['genre_ids']:
        new.append(movie)

with open('wars.json', 'w', encoding='utf-8') as make_file:
    json.dump(new, make_file, ensure_ascii=False, indent="\t")

