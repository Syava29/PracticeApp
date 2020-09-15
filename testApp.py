from docxtpl import DocxTemplate
from tkinter import *
from tkinter import scrolledtext


""" Бизнес_логика приложения"""
def getText():
    s = entry.get()
    doc = DocxTemplate("RPD_test.docx")
    context = {'prepod': s}
    doc.render(context)
    doc.save("RPD_final.docx")
    label['text'] = s


""" Визуализация """

window = Tk()
window.title("Генератор Рабочей программы дисциплины")
window.geometry('1500x500')

frm_form = Frame(relief=SUNKEN, borderwidth=3)
frm_form.pack()

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
# Создает текстовое поле которая соответствует ярлыку.
entry = Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыков и
# текстовых полей в строку, чей индекс равен idx.
label.grid(row=1, column=0, sticky="e")
entry.grid(row=1, column=1)




frm_buttons = Frame()
frm_buttons.pack(fill=X, ipadx=5, ipady=5)

btn_submit = Button(master=frm_buttons, text="Добавить")
btn_submit.pack(side=RIGHT, padx=10, ipadx=10)

btn_clear = Button(master=frm_buttons, text="Отчистить")
btn_clear.pack(side=RIGHT, ipadx=10)

label = Label()
label.pack(side=LEFT)
text = Text(window, width=20, height=2)
text.pack(side=LEFT)


b_get = Button(window, text="Взять", command=getText)
b_get.pack(side=RIGHT)




window.mainloop()

