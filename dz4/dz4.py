import math
import random


def task1():
    p = 3.
    it = 1 
    for i in range(2,56,2):

        p+=(it * 4.)/(i*(i+1.)*(i+2.))
        it*=-1.
    print(p)
    

def task2():
    count = int(input("Укажите число : "))
    mn = []
    while count > 0 :
        for i in range(2,10):
            if count%i == 0 :
                mn.append(i)
                count //= i
                break
            elif(i == 9):
                mn.append(count)
                count=0
    print(*mn)


def task3():
   my_list = [123, 321, 214, 324, 3, 434, 34, 34, 324, 325, 4565, 745, 8, 98, 8, 79, 87, 98, 9]
   print(*set(my_list))

def task4():
   n = random.randint(2, 8)
   coef = []
   for i in range(1, n+2):
       coef.append(random.randint(1, 100))
   with open('task5-2.txt', mode='w', encoding='utf-8')  as file :
       file.write(f" {' + '.join([ f' {item}x^{number+1}' for number ,item in  enumerate(coef[:1:-1])][::-1])} + {coef[1]}x + {coef[0]} = 0")
       file.close()



def task5():
    def parseStr(strok,slov=dict()):
        for item in strok:
            if 'x^' in item:
                coun, key = item.split('x^')
                if key in slov:
                    slov[key] += int(coun)
                else:
                    slov[key] = int(coun)
            elif 'x' in item:
                coun = item.split('x')[0]
                if 'one' in slov:
                    slov['one'] += int(coun)
                else:
                    slov['one'] = int(coun)
            else:
                coun = int(item)
                if 'free' in slov:
                    slov['free'] += int(coun)
                else:
                    slov['free'] = int(coun)
        return slov


    with open('task5-2.txt', mode='r', encoding='utf-8') as file:
        mn1 = file.read()
        file.close()
    with open('task5.txt', mode='r', encoding='utf-8') as file:
        mn2 = file.read()
        file.close()
    print(mn1)
    print(mn2)

    mn1 = mn1.split('=')[0].replace(' ', '').split('+')
    mn2 = mn2.split('=')[0].replace(' ', '').split('+')
    dictKey = parseStr(mn1)
    dictKey = parseStr(mn2, dictKey)


    numberKeys = [int(key) for key in dictKey.keys() if not key in ['one','free'] ]
    numberKeys.sort(reverse=True)

    newSTR = [ f"{dictKey[str(key)]}x^{key} "  for key in numberKeys]

    with open('task6.txt', mode='w', encoding='utf-8') as file:
        file.write(' + '.join(newSTR) + f" + {dictKey['one']}x + " + str(dictKey['free']))
        file.close()







def startMenu():
    """Меню для выбра задачи"""
    tasks = [
        {"func" : task1,
         "text": """Ввычислить число пи"""},
        {"func": task2,
         "text": """Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""},
         {"func": task3,
         "text": """ Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности."""},
        {"func":task4,
        "text": """ Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0"""},
        {"func": task5,
             "text": """  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)"""},
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
