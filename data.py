import json

with open('it_dict.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

DataSet = set(data)

if __name__ == '__main__':
    print(DataSet)
    print()
    for id in data.items():
        print(id)
