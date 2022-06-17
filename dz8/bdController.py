import json
import os


def loadTable(tableName):
    if os.path.exists(f"./bd/{tableName}.json"):
        with open(f"./bd/{tableName}.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        return []

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

