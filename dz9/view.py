from tkinter import *
from controller import funcCalc


def generationTablo(param=''):
    text = funcCalc(param)
    print(f'{param=}')
    print(f'{text=}')
    label = Label(text=f'{text:40}')
    label.grid(row=0, column=0, columnspan=4)

def generationButton():
    listButtonText = ["C","Del","(",")",
                      "7","8","9","/",
                      "4","5","6","*",
                      "1","2","3","",
                      "0","+","-","="]

    row = 5
    col = 4
    listButton=[]
    for r in range(row):
        for c in range(col):
            textbtn = listButtonText[r*4+c]


            listButton.append(Button(text=textbtn, bg="#FFF",
               font=("Times New Roman", 35),
               command = lambda t=textbtn: generationTablo(f'{t}')
                         ).grid(row=r+1, column=c, columnspan=1))



