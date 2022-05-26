from datetime import datetime

def task1():
    number = int(input("Укажите число: "))
    numberSeries = [1,]
    for i in range(2, number+1):
        numberSeries.append(i * numberSeries[i-2])
    print(*numberSeries)



def task2():
    number = int(input("Укажите число: "))
    summ =0
    for i in range(1,number+1):
        summ += (1+1/i)**i
    print(summ)

def task3():
    my_list = [5,7,5,4,23,43,536,657,8,54,6]
    print(my_list)
    print()
    for i in range(len(my_list)):
        rand_i = i//2+(len(my_list)-i)//(datetime.now().microsecond % 10 + 1)
        my_list[i] , my_list[rand_i] = my_list[rand_i], my_list[i]

    print(my_list)







def startMenu():
    """Меню для выбра задачи"""
    tasks = [
        {"func" : task1,
         "text": """Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""},
        {"func": task2,
         "text": """Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму."""},
         {"func": task3,
         "text": """Реализуйте алгоритм перемешивания списка"""},

    ]

    menuText = '\n'.join([ f"{id+1}. {item['text']}"  for id,item in enumerate(tasks)]) + "\nВыберите номер задачи: "
    choise = input(menuText)
    try:
        choise = int(choise)-1
    except:
        print("ввели не число")
        return "Error"
    if choise >= len(tasks) or choise < 0:
        print("ввели неправильное число")
        return "Error"
    tasks[choise]["func"]()




if __name__=="__main__":
    startMenu()
