import xlrd
from collections import OrderedDict
import json
import openpyxl
import pandas


# Windows용 excel_path = '‪C:\\Users\\user\\Desktop\\rpa\\json_to_excel.xlsx'
excel_path = 'c:\\Users\\tjdwn\\OneDrive\\바탕 화면\\TIL\\python_excel을json으로변환\\영양성분.xlsx'

# excel_path = 'C:\\Users\\tjdwn\\OneDrive\\Desktop\\TIL\\영양성분.xlsx'
# excel_path = '\영양성분.xlsx'
# excel_path = excel_path[1:]
wb = pandas.read_excel(excel_path, engine="openpyxl")
sh = wb.sheet_by_index(0)

data_list = []

for rownum in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    data['식품명'] = row_values[0]
    # data['url'] = row_values[1]
    # data['top'] = row_values[2]
    # data['left'] = row_values[3]
    # data['width'] = row_values[4]
    # data['height'] = row_values[5]
    data_list.append(data)

j = json.dumps(data_list, ensure_ascii=False)

with open('/Users/tjdwn/OneDrive/바탕 화면/data.json', 'w+') as f:
    f.write(j)