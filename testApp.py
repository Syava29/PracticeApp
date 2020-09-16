from docxtpl import DocxTemplate
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Tk, BOTH, Menu
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox

""" Бизнес_логика приложения"""
def getText():
    prepod_get = entry.get()
    discip_get = combobox_discip.get()
    type_ed_prog_get = combobox_ed_prog.get()
    doc = DocxTemplate("RPD_test.docx")
    context = {'prepod': prepod_get, 'discip': discip_get, 'type_ed_prog': type_ed_prog_get}
    doc.render(context)
    doc.save("RPD_final.docx")




def deleteText():
    entry.delete(0, END)


def newWindow():
    window = Tk()
    window.title("Генератор Рабочей программы дисциплины")
    window.geometry('1000x500')






""" Визуализация """

window = Tk()
window.title("Генератор Рабочей программы дисциплины")
window.geometry('600x600')

frm_form = Frame(relief=SUNKEN, borderwidth=3)
frm_form.pack(fill=X, ipadx=5, ipady=5, padx=10)

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
#entry_1 = Entry(master=frm_form, width=50)
#entry_2 = Entry(master=frm_form, width=50)
#entry_3 = Entry(master=frm_form, width=50)
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
#entry_1.grid(row=2, column=1)
#entry_2.grid(row=3, column=1)
#entry_3.grid(row=4, column=1)
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





label = Label()
label.pack(side=LEFT)


window.mainloop()

