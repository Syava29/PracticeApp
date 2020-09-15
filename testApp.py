from docxtpl import DocxTemplate
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Tk, BOTH
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
    main()



def deleteText():
    entry.delete(0, END)


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Всплывающие окна с уведомлениями")
        self.pack()

        error = Button(self, text="Ошибка", command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Предупреждение", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Вопрос", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Информация", command=self.onInfo)
        inform.grid(row=1, column=1)

    def onError(self):
        mbox.showerror("Ошибка", "Не могу открыть файл")

    def onWarn(self):
        mbox.showwarning("Предупреждение", "Вызов устаревшей функции")

    def onQuest(self):
        mbox.askquestion("Вопрос", "Вы уверены, что хотите выйти?")

    def onInfo(self):
        mbox.showinfo("Информация", "Скачивание завершено")


def main():
    root = Tk()
    ex = Example()
    root.geometry("300x150+300+300")
    root.mainloop()







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
label_1 = Label(master=frm_form, text=labels[1])
label_2 = Label(master=frm_form, text=labels[2])
label_3 = Label(master=frm_form, text=labels[3])
label_4 = Label(master=frm_form, text=labels[4])
label_5 = Label(master=frm_form, text=labels[5])

# Создает текстовое поле которая соответствует ярлыку.
entry = Entry(master=frm_form, width=50)
#entry_1 = Entry(master=frm_form, width=50)
#entry_2 = Entry(master=frm_form, width=50)
entry_3 = Entry(master=frm_form, width=50)
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
entry_3.grid(row=4, column=1)
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
                                    "специалитет, магистратура",])
combobox_ed_prog.grid(row=3, column=1)


frm_buttons = Frame()
frm_buttons.pack(fill=X, ipadx=5, ipady=5)

btn_submit = Button(master=frm_buttons, text="Добавить", command=getText)
btn_submit.pack(side=RIGHT, padx=10, ipadx=10)

btn_clear = Button(master=frm_buttons, text="Отчистить", command=deleteText)
btn_clear.pack(side=RIGHT, ipadx=10)





label = Label()
label.pack(side=LEFT)


window.mainloop()

