import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    print(json_data[4])
    print(len(json_data))

    # for i in range(len(json_data)):
    #     if json_data[i]['식품명'] == '육회':
    #         print(json_data[i])
    #         print(i)