import math

def task1():
    indexDay = int(input("Укажите день недели: "))
    if indexDay == 6 or indexDay == 7:
        print("Выходной")
    elif indexDay > 0 and indexDay < 6:
        print("Рабочий день")
    else:
        print("Неправильно указали возраст")
def task2():
    x = int(input("Укажите значение x: "))
    y = int(input("Укажите значение y: "))
    z = int(input("Укажите значение z: "))
    print(not (x or y or z) == (not x and not y and not z))

def task3():
    x = int(input("Укажите значение x: "))
    y = int(input("Укажите значение y: "))
    if x == 0 or y == 0:
        print("x или y не могут быть равны 0")
        return "Error"
    if x > 0 and y >0 :
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)

def task4():
    quarter = int(input("Укажите четверть"))
    if quarter == 1:
        print("X = (0;∞] , y = (0;∞]")
    elif quarter == 2:
        print("X = (0;-∞] , y = (0;∞]")
    elif quarter == 3:
        print("X = (0;-∞] , y = (0;-∞]")
    elif quarter == 4:
        print("X = (0;∞] , y = (0;-∞]")
    else:
        print("указано неправильное значение")


def task5():
    x = input("Укажите координаты x через запятую: ").split(',')
    y = input("Укажите координаты y через запятую").split(',')
    print(x)
    print(y)
    lenght = math.sqrt((int(x[1]) - int(x[0]))**2 + (int(y[1]) - int(y[0]))**2)
    print(lenght)





def startMenu():
    """Меню для выбра задачи"""
    tasks = [
        {"func" : task1,
         "text": """Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным."""},
        {"func": task2,
         "text": """Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."""},
         {"func": task3,
         "text": """Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)."""},
        {"func":task4,
        "text": """Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."""},
        {"func": task5,
             "text": """Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве."""},
    ]

    menuText = "Выберите номер задачи: \n " + '\n'.join([ f"{id+1}. {item['text']}"  for id,item in enumerate(tasks)])
    choise = input(menuText)
    try:
        choise = int(choise)-1
    except:
        print("ввели не число")
        return "Error"
    if choise >= len(tasks) or choise<1:
        print("ввели неправильное число")
        return "Error"
    tasks[choise]["func"]()




if __name__=="__main__":
    startMenu()
