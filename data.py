import json
import pandas

excel_data = pandas.read_excel('it_dict.xlsx',)
json_data = excel_data.to_json(orient='index', force_ascii=False)
data = json.loads(json_data)

DataSet = set(data)

if __name__ == '__main__':
    print(DataSet)
    print()
    for id in data.items():
        print(id)
        