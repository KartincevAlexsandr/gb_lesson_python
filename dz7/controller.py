
import json
from datetime import datetime

import dbController


def importToFile(path):
    name, type = path.split('.')
    if type == 'csv':
        with open(path, 'r', encoding='utf8') as file:
            text = file.read()
        data = [item.split(';')[1:]  for item in text.split('\n')]


    elif type == 'json':
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data = list(map(lambda i: i[1:], data))
            print(data)


    elif type == 'html':
        with open(path, 'r', encoding='utf8') as file:
            text = file.read()

        text = text.split('<body><tr>')[1].split('</tr></body>')[0].split('</tr><tr>')
        data = [item.split('</td><td>')[1:] for item in text]

    else:
        return 0

    for item in data:
        item[-1] = datetime.now()
        dbController.addToDB(item)

def exportFile(type='csv', path='myFile'):
    data = dbController.loadDB()
    if type == 'csv':
        text = '\n'.join([';'.join(item)for item in data])
        with open(path+'.'+type , 'w', encoding='utf8') as file:
            file.write(text)

    elif type == 'json':
        with open(path + '.'+type, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))

    elif type == 'html':
        text = '''<table><head><tr><th>id</th><th>Фамилия</th><th>Имя</th><th>Отество</th><th>Телефон</th><th>Описание</th><th>добавлен</th></tr></head><body>'''
        text +=   '<tr>' + '</tr><tr>'.join(['<td>' + '</td><td>'.join(item) + '</td>' for item in data])+ '</tr>'
        text +="</body></table>"

        with open(path + '.' + type, 'w', encoding='utf8') as file:
            file.write(text)




