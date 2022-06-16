import json
import os



def loadDB():
    if os.path.exists('mydb.mydb'):
        with open('mydb.mydb', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        return []



def saveDB(data):
    with open('mydb.mydb', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
    return 'ok'

def addToDB(item):
    data = loadDB()
    if len(data) > 0:
        id = int(data[-1][0] )+ 1
    else:
        id = 0
    item= [id] + item
    item = list(map(lambda i: str(i), item))
    data.append(item)
    saveDB(data)
    return data

def delDB(id):
    data = loadDB()
    try:
        data.remove(*(filter(lambda item: item[0] == str(id), data)))
        saveDB(data)
    except:
        print('ввели несуществующий id')
    return data

def findDB(text):
    data = loadDB()
    findList = filter(lambda item: len([key for key in item if text.lower() in key.lower()]) > 0, data)
    return findList