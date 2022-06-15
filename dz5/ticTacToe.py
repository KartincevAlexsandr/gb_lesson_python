from pprint import pprint

dictCell = {
    'a': 0,
    'b': 1,
    'c': 2
}

def checkIsFin(m):
    for i in range(len(m)):
        if m[i][0] == m[i][1] == m[i][2] and m[i][0] != '':
            return True
        if m[0][i] == m[1][i] == m[2][i] and m[0][i] != '':
            return True
    if m[0][0] == m[1][1] == m[2][2] and m[0][0] != '':
        return True
    if m[0][2] == m[1][1] == m[2][0] and m[0][2] != '':
        return True
    return False

def printField(m):
    print("\\ A | B | C")
    for i in range(len(m)):
        print(f"-------------")
        print(f"{i+1} | {m[i][0]} | {m[i][1]} | {m[i][2]} |")

def startgame():
    playingField = [['', '', ''] for i in range(3)]
    limitTic = 9
    pprint(playingField)
    tickName = 'Игрок 1'
    printField(playingField)
    while limitTic > 0:
        cell = input("Укажите ячейку, пример 'A1' : ")
        try:
            cell = [int(cell[1])-1, int(dictCell.get(cell[0].lower()))]
        except:
            print("Неправильно указана ячейка")
            continue
        if playingField[cell[0]][cell[1]] != '':
            print("Ячейка занята")
            continue
        playingField[cell[0]][cell[1]] = 'X' if tickName == 'Игрок 1' else 'O'
        if checkIsFin(playingField):
            print(f"{tickName} выиграл")
            printField(playingField)
            return 1

        tickName = 'Игрок 2' if tickName == 'Игрок 1' else 'Игрок 1'
        printField(playingField)
        limitTic -=1
    print("Ничья")
















if __name__ == "__main__":
    startgame()