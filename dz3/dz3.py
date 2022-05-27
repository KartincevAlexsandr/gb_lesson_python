import math

def task1():
    def sumList(l):
        return sum(l[1::2])
    my_list = [123, 321, 214, 324, 3, 434, 34, 34, 324, 325, 4565, 745, 8, 98, 8, 79, 87, 98, 9]
    print(sumList(my_list))

def task2():
    my_list = [123, 321, 214, 324, 3, 434, 34, 34, 324, 325, 4565, 745, 8, 98, 8, 79, 87, 98, 9]
    print([my_list[i] * my_list[-i-1] for i in range(math.ceil(len(my_list) / 2))])

def task3():
    my_list = [1.1, 1.2, 3.1, 5, 10.01]
    maxFloat = max([item % 1 for item in my_list])
    minFloat = min([item % 1 for item in my_list])
    print(maxFloat-minFloat)

def task4():
    def getMyBoolean(number):
        while number > 0:
            yield number % 2
            number = number // 2

    for b in getMyBoolean(45):
        print(b,end='')
    print('\n')


def task5():


    count = int(input("Укажите число : "))

    fibonaci = []
    for i in range(count):
        if i == 0 or i == 1:
            fibonaci.append(1)
        else:
            fibonaci.append(fibonaci[-2] + fibonaci[-1])

    nefaFibonachi = []
    for i in range(count):

        if i == 0 :
            nefaFibonachi.append(1)
        elif i == 1:
            nefaFibonachi.append(-1)
        else:
            nefaFibonachi.append((nefaFibonachi[-1] - nefaFibonachi[-2] )* (-1))

    print(nefaFibonachi[::-1]+fibonaci)
1






def startMenu():
    """Меню для выбра задачи"""
    tasks = [
        {"func" : task1,
         "text": """Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции."""},
        {"func": task2,
         "text": """Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д."""},
         {"func": task3,
         "text": """ Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""},
        {"func":task4,
        "text": """ Напишите программу, которая будет преобразовывать десятичное число в двоичное. """},
        {"func": task5,
             "text": """  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""},
    ]

    menuText = "Выберите номер задачи: \n " + '\n'.join([ f"{id+1}. {item['text']}"  for id,item in enumerate(tasks)])
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




if __name__=="__main__":
    startMenu()
