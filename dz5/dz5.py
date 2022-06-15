import lorem
import candyGame
import ticTacToe


def task1():
    t = lorem.text()
    t = ' '.join([char for char in t.split() if not 'abc' in char.lower()])
    print(t)


def task2():
    candyGame.startgame()


def task3():
    ticTacToe.startgame()


def task4():
    def compression():
        with open('file1.txt','r') as file:
            text = file.read()
        compression = ''
        repetition = 0
        tempChar = text[0]
        for i in text:
            if i == tempChar:
                repetition += 1
            else:
                compression += tempChar + str(repetition)
                repetition = 1
                tempChar = i
        with open('file_compression.txt','w') as file:
            file.write(compression)

    def restore():
        with open('file_compression.txt', 'r') as file:
            text = file.read()
        restore = ''
        for i in range(0, len(text), 2):
            restore += text[i] * int(text[i+1])
        with open('file_restore.txt','w') as file:
            file.write(restore)


    ation = int(input("Необходимо сжать -1 , востановить данные - 2"))
    if ation == 1:
        compression()
    elif ation == 2:
        restore()





def startMenu():
    """Меню для выбра задачи"""
    tasks = [
        {"func": task1,
         "text": """Напишите программу, удаляющую из текста все слова, содержащие "абв"."""},
        {"func": task2,
         "text": """Создайте программу для игры с конфетами человек против человека."""},
        {"func": task3,
         "text": """ Создайте программу для игры в "Крестики-нолики"."""},
        {"func": task4,
         "text": """ Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""}  ]

    menuText = "Выберите номер задачи: \n " + '\n'.join([f"{id + 1}. {item['text']}" for id, item in enumerate(tasks)])
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


if __name__ == "__main__":
    startMenu()
