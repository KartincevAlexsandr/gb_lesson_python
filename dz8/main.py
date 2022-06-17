from tkinter import *
from  tkinter import ttk
from tkinter import messagebox

import bdController






window = Tk()
window.title("ДЗ 8")
myvar = StringVar()
myvar.set('')
elements = []

def openEmplyees(tablename):
    data = bdController.loadTable(tablename)
    clearWindow()
    window.geometry("1200x400")
    elements.append(Button(
        text="Назад",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73'
    ))
    elements[-1].bind('<Button-1>', startMenu)
    elements[-1].grid(row=1,column=1,columnspan=1)


    tables = ttk.Treeview(window)
    tables['columns'] = list(data[0].keys())

    tables.heading("#0", text="", anchor=CENTER)
    tables.column("#0", width=0, stretch=NO)

    for key in tables['columns'] :
        tables.column(key, anchor=CENTER, width=80)
        tables.heading(key, text=key, anchor=CENTER)
    id = 0
    for item in data:
        tables.insert(parent='', index='end', iid=id, text='',
                                      values= [item[k] for k in tables['columns']] )
        id+=1
    elements.append(tables)
    tables.grid(row=3,column=1,columnspan=10)

    ###############   Кнопка редактировать сотрудника
    elements.append(Button(
        text="Редактировать",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73'
    ))
    elements[-1].bind('<Button-1>', editCell)
    elements[-1].grid(row=4, column=1, columnspan=1)

    ###############   Кнопка добавить сотрудника
    elements.append(Button(
        text="Добавить",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73',
        command=lambda: addCell(tables['columns'],tablename)
    ))
    elements[-1].grid(row=4,column=2,columnspan=1)

    ###############   Кнопка удалить сотрудника
    elements.append(Button(
        text="Удалить",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73'
    ))
    elements[-1].bind('<Button-1>', dellCell)
    elements[-1].grid(row=4, column=3, columnspan=1)

def addCell(rableName,tablename):
    def save(data):
        for key in data.keys():
            data[key] = data[key].get("1.0", "end-1c")

        bdController.addCell(tablename, data)
        newWindow.destroy()
        openEmplyees(tablename)


    newWindow = Toplevel(window)
    newWindow.title("Добавить струдника")
    newWindow.geometry("900x200")
    newData = {}
    for k in rableName:
        if k == 'id':
            continue
        newData[k] = Text(newWindow, height=1, width=12)
    for number, key in enumerate(newData.keys()):
        lbl = Label(newWindow, text=key, font=("Arial Bold", 12))
        lbl.grid(column=number, row=0)
    for number, key in enumerate(newData.keys()):
        newData[key].grid(column=number, row=1)

    ###############   Кнопка сохранить нового сотрудника
    btnsave = Button(newWindow,
        text="Сохранить",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73',
                     command= lambda: save(newData)
    )
    btnsave.bind('<Button-1>')
    btnsave.grid(column=0, row=3)



    print('add')

def dellCell(event):
    print('dell')

def editCell(event):
    print('edit')

def clearWindow():
    for i in range(len(elements)):
        e = elements.pop()
        e.grid_forget()

def startMenu(event=None):
    window.geometry("200x100")
    clearWindow()
    elements.append(Button(
        text="Просмотр списка сотрудников",
        bg="#ccc",
        fg = "#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73',
        command=lambda: openEmplyees('emplyees')
    ))
    elements.append(Button(
        text="Подразделения",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73',
        command=lambda: openEmplyees('sudbivision')
    ))
    elements.append(Button(
        text="График",
        bg="#ccc",
        fg="#3d3d42",
        activebackground="#eff5c9",
        activeforeground='#6e6f73',
        command=lambda: openEmplyees('schedule')
    ))

    for i in range(len(elements)):
        elements[i].grid(row=i,column=2,columnspan=5)





startMenu()


















window.mainloop()