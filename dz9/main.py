from tkinter import *

from view import generationButton,generationTablo
from controller import resolution





if __name__ == '__main__':
    print("stert GUI")
    window = Tk()
    window.title("ДЗ 9 Калькулятор")
    window["bg"] = "#000"
    window.geometry("400x400")

    generationButton()
    generationTablo()

    window.mainloop()