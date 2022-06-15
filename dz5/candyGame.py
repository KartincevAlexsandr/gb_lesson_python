import random
import math


def botGetNumber(min,max,count=0):
    if count==0:
        return random.randint(min, max+1)

    if count > max*2:
        return max
    elif count> max:
        return count - max - 1
    return count


def inputPlayer(min,max,text='Для жеребьевки'):
    while True:
        try:
            number = int(input(text + f" введите число от {min} до {max}  "))
        except:
            continue
        if number >= min and number <= max:
            return number
        print("Неверно указано число\n")






def startgame():
    isBot = input("1. играть с ботом.\n2. Играть со в торым игроком\nВведите номер: ") == '1'
    countCandy = 321

    player1 = inputPlayer(1, 10, 'Игрок 1. Для жеребьевки')
    if not isBot:
        player2 = inputPlayer(1, 10, 'Игрок 2. Для жеребьевки')
    else:
        player2 = botGetNumber(1, 10)
    randomNumber = random.randint(1, 11)
    playerlit = []
    if abs(randomNumber-player1) < abs(randomNumber-player2):
        tickName = 'Игрок 1'
    else:
        tickName = 'Игрок 2'

    print(f"Первым ходит {tickName}")
    while countCandy > 0:
        if tickName == 'Игрок 2' and isBot:
            number = botGetNumber(1,28,countCandy)
            if countCandy - number <=0:
                print(f"бот выбрал {number}, бот выиграл!")
                break
            print(f"бот выбрал {number} осталось {countCandy-number}")
            countCandy-=number
            tickName = 'Игрок 2' if tickName == 'Игрок 1' else 'Игрок 1'
            continue

        number = inputPlayer(1, 28, f'{tickName}. ')
        if countCandy - number <=0:
            print(f"{tickName} выбрал {number}, {tickName} выиграл!")
            break
        print(f"{tickName} выбрал {number} осталось {countCandy-number}")
        countCandy -= number
        tickName = 'Игрок 2' if tickName == 'Игрок 1' else 'Игрок 1'


if __name__ == "__main__":
    startgame()