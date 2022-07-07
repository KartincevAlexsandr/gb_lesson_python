import json
import os


def loadTable(tableName):
    if os.path.exists(f"./bd/{tableName}.json"):
        with open(f"./bd/{tableName}.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        return []


def loadTableJoin(tableName):
    print(1)
    with open(f"./bd/emplyees.json", 'r', encoding='utf-8') as file:
        data_emplyees = json.load(file)
    with open(f"./bd/sudbivision.json", 'r', encoding='utf-8') as file:
        data_sudbivision = json.load(file)


    for item in data_emplyees:
        city = list(filter(lambda x: x["id"] == item["location"],data_sudbivision))
        if len(city) == 1:
            item["Название подразделения"] = city[0]["Название"]
            item["Город"] = city[0]["Город"]
            item["Улица"] = city[0]["Улица"]
            item["Дом"] = city[0]["Дом"]
        else:
            item["Название подразделения"] = ''
            item["Город"] = ''
            item["Улица"] = ''
            item["Дом"] = ''
    return data_emplyees

def transactionTable(tableName,data):
    with open(f"./bd/{tableName}.json", 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
    return 'ok'

def addCell(tableName,cell):
    data = loadTable(tableName)
    if len(data) > 0:
        id = int(data[-1]['id']) + 1
    else:
        id = 0
    cell["id"] = id
    data.append(cell)
    transactionTable(tableName, data)
    return "ok"

def delCell(tableName,cell):
    pass

def joinTable(Table1,row,table2,row2):
    pass

