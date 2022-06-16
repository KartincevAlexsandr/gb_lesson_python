import dbController
import controller
from datetime import datetime
import os
from model import Users

def displayData():
    ### Отрисовываем таблицу в консоль
    data = dbController.loadDB()
    print( '\n'.join(  [ ' | '.join(item) for  item in data]) )

def find():
    ### Ищем по включение фразы и отрисовываем таблицу в консоль
    key = input("Укажите словодля поиска:  ")
    data = dbController.findDB(key)
    print('\n'.join([' | '.join(item) for item in data]))

def addNewUser():
    print("Добавления новой записи")
    listKey = ['Введите фамилию: ', 'Введите имя: ', 'Введите отчество: ', 'Введите телефон: ', 'Введите описание: ']
    user = []
    for key in listKey:
        user.append(input(key))
    user.append(datetime.now())
    data = dbController.addToDB(user)
    displayData()


def dellUser():
    key = input("Укажите номер строки для удаления")
    data = dbController.delDB(key)
    displayData()

def importToFile():
    while True:
        name = input("Укажите название файла: ")
        if os.path.exists(name):
            break
        print("Данный файл не существует")
    controller.importToFile(name)
    print("export ok")


def exportFile():
    name = input("Укажите название файла: ")
    listType = ['csv', 'json', 'html']
    while True:
        print('Укажите тип данных ')
        type = input('\n'.join(listType) + '\n ')
        if type in listType:
            break
    controller.exportFile(type, name)
    print("export ok")


def exit():
    raise SystemExit(1)

def startMenu():

    """Меню"""
    tasks = [
        {"func": displayData,
         "text": """Отобразить все данные"""},
        {"func": find,
         "text": """Поиск"""},
        {"func": addNewUser,
         "text": """Добавить запись"""},
        {"func": dellUser,
         "text": """Удалить запись"""},
        {"func": exportFile,
         "text": """Экспортировать данные из БД"""},
        {"func": importToFile,
         "text": """Импорт данных в БД"""},
         {"func": exit,
         "text": """Выйти"""}
    ]

    while True:
        menuText = "Меню: \n" + '\n'.join(
            [f"{id + 1}. {item['text']}" for id, item in enumerate(tasks)])
        choise = input(menuText)
        try:
            choise = int(choise) - 1
        except:
            print("ввели не число")
            return "Error"
        if choise >= len(tasks) or choise < 0:
            print("ввели неправильное число")
            return "Error"
        tasks[choise]["func"]()

