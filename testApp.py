from docxtpl import DocxTemplate
from tkinter import *
from tkinter import scrolledtext, Frame, Tk, BOTH, Text, Menu, END
from tkinter import ttk, filedialog
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox
import docx as dc

""" Бизнес_логика приложения"""


def getText():
    prepod_get = entry.get()
    discip_get = combobox_discip.get()
    type_ed_prog_get = combobox_ed_prog.get()
    doc = DocxTemplate("RPD_test.docx")
    context = {'prepod': prepod_get, 'discip': discip_get, 'type_ed_prog': type_ed_prog_get}
    doc.render(context)
    doc.save("RPD_final.docx")
    document = dc.Document("RPD_final.docx")
    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    mainText.insert('1.0', fullText)


def deleteText():
    entry.delete(0, END)


def newWindow():
    window = Tk()
    window.title("Генератор Рабочей программы дисциплины")
    window.geometry('600x600')


def onOpen():
    ftypes = [('py файлы', '*.py'), ('Все файлы', '*')]
    dlg = filedialog.Open(window, filetypes=ftypes)
    fl = dlg.show()
    fll = open(fl)
    fl2 = fll.readline()
    mainText.insert(1.0, fl2)


""" Визуализация """
window = Tk()
window.title("Генератор Рабочей программы дисциплины")
window.geometry('600x600')

# создание меню
menubar = Menu(window.master)
window.config(menu=menubar)

fileMenu = Menu(menubar)
fileMenu.add_command(label="Открыть файл", command=onOpen)

menubar_label = [
    "Цели и задачи освоения дисциплины",
    "Место дисциплины в структуре ОП",
    "Планируемые результаты обучения по дисциплине",
    "Структура дисциплины и распределение её трудоёмкости"
]

description_menu_bar = Menu(menubar)
description_menu_bar.add_command(label="Цели и задачи освоения дисциплины", command=newWindow)
description_menu_bar.add_command(label=menubar_label[0], command=newWindow)
description_menu_bar.add_command(label=menubar_label[1], command=newWindow)
description_menu_bar.add_command(label=menubar_label[2], command=newWindow)
description_menu_bar.add_command(label=menubar_label[3], command=newWindow)

menubar.add_cascade(label="Файл", menu=fileMenu)
menubar.add_cascade(label="Содержание РПД", menu=description_menu_bar)

# Создание Рамки с лэйблами и текстовыми полями
frm_form = Frame(relief=SUNKEN, borderwidth=3)
frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)

labels = [
    "ФИО:",
    "Дисциплина:",
    "Тип образовательной программы:",
    "Форма обучения:",
    "Направление подготовки:",
    "Профиль:",
]

# Создает ярлык с текстом из списка ярлыков.
label = Label(master=frm_form, text=labels[0])
label_1 = Label(master=frm_form, text=labels[1])
label_2 = Label(master=frm_form, text=labels[2])
label_3 = Label(master=frm_form, text=labels[3])
label_4 = Label(master=frm_form, text=labels[4])
label_5 = Label(master=frm_form, text=labels[5])

# Создает текстовое поле которая соответствует ярлыку.
entry = Entry(master=frm_form, width=50)
# entry_1 = Entry(master=frm_form, width=50)
# entry_2 = Entry(master=frm_form, width=50)
# entry_3 = Entry(master=frm_form, width=50)
entry_4 = Entry(master=frm_form, width=50)
entry_5 = Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыков и
# текстовых полей в строку, чей индекс равен idx.
label.grid(row=1, column=0, sticky="e")
label_1.grid(row=2, column=0, sticky="e")
label_2.grid(row=3, column=0, sticky="e")
label_3.grid(row=4, column=0, sticky="e")
label_4.grid(row=5, column=0, sticky="e")
label_5.grid(row=6, column=0, sticky="e")

entry.grid(row=1, column=1)
# entry_1.grid(row=2, column=1)
# entry_2.grid(row=3, column=1)
# entry_3.grid(row=4, column=1)
entry_4.grid(row=5, column=1)
entry_5.grid(row=6, column=1)

combobox_discip = ttk.Combobox(frm_form, values=[
    "Программирование",
    "Философия",
    "Эконометрика",
    "Иностранный язык"])
combobox_discip.grid(row=2, column=1)

combobox_ed_prog = ttk.Combobox(frm_form, values=[
    "бакалавриат",
    "специалитет, магистратура"])
combobox_ed_prog.grid(row=3, column=1)

combobox_form_ed = ttk.Combobox(frm_form, values=[
    "очная",
    "очно-заочная",
    "заочная"])
combobox_form_ed.grid(row=4, column=1)

frm_buttons = Frame()
frm_buttons.pack(fill=X, ipadx=5, ipady=5)

btn_submit = Button(master=frm_buttons, text="Добавить", command=getText)
btn_submit.pack(side=LEFT, padx=10, ipadx=10)

btn_clear = Button(master=frm_buttons, text="Отчистить", command=deleteText)
btn_clear.pack(side=LEFT, padx=10, ipadx=10)

btn_nw = Button(master=frm_buttons, text="New", command=newWindow)
btn_nw.pack(side=LEFT, padx=10, ipadx=10)

mainText = Text(window)
mainText.pack()

scroll = Scrollbar(command=mainText.yview)
scroll.pack(side=LEFT, fill=Y)

mainText.config(yscrollcommand=scroll.set)

label = Label()
label.pack(side=LEFT)

window.mainloop()
