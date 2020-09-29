from tkinter import *
from tkinter import Tk, Text, END
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.ttk import Frame, Button

import docx as dc
from docxtpl import DocxTemplate

from second_window import SecondWindow


class MainWindow:
    def __init__(self, width, height, title="Генератор Рабочей программы дисциплины", resizable=(False, False),
                 icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)



        self.frm_form = Frame(relief=SUNKEN, borderwidth=3)
        self.frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)

        self.labels = [
            "ФИО:",
            "Дисциплина:",
            "Тип образовательной программы:",
            "Форма обучения:",
            "Направление подготовки:",
            "Профиль:",
        ]

        # Создает ярлык с текстом из списка ярлыков.
        self.label = Label(master=self.frm_form, text=self.labels[0])
        self.label_1 = Label(master=self.frm_form, text=self.labels[1])
        self.label_2 = Label(master=self.frm_form, text=self.labels[2])
        self.label_3 = Label(master=self.frm_form, text=self.labels[3])
        self.label_4 = Label(master=self.frm_form, text=self.labels[4])
        self.label_5 = Label(master=self.frm_form, text=self.labels[5])

        # Создает текстовое поле которая соответствует ярлыку.
        self.entry = Entry(master=self.frm_form, width=50)
        # entry_1 = Entry(master=frm_form, width=50)
        # entry_2 = Entry(master=frm_form, width=50)
        # entry_3 = Entry(master=frm_form, width=50)
        self.entry_4 = Entry(master=self.frm_form, width=50)
        self.entry_5 = Entry(master=self.frm_form, width=50)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        self.label.grid(row=1, column=0, sticky="e")
        self.label_1.grid(row=2, column=0, sticky="e")
        self.label_2.grid(row=3, column=0, sticky="e")
        self.label_3.grid(row=4, column=0, sticky="e")
        self.label_4.grid(row=5, column=0, sticky="e")
        self.label_5.grid(row=6, column=0, sticky="e")

        self.entry.grid(row=1, column=1)
        # entry_1.grid(row=2, column=1)
        # entry_2.grid(row=3, column=1)
        # entry_3.grid(row=4, column=1)
        self.entry_4.grid(row=5, column=1)
        self.entry_5.grid(row=6, column=1)

        self.combobox_discip = ttk.Combobox(self.frm_form, values=[
            "Программирование",
            "Философия",
            "Эконометрика",
            "Иностранный язык"])
        self.combobox_discip.grid(row=2, column=1)

        self.combobox_ed_prog = ttk.Combobox(self.frm_form, values=[
            "бакалавриат",
            "специалитет, магистратура"])
        self.combobox_ed_prog.grid(row=3, column=1)

        self.combobox_form_ed = ttk.Combobox(self.frm_form, values=[
            "очная",
            "очно-заочная",
            "заочная"])
        self.combobox_form_ed.grid(row=4, column=1)

        self.frm_buttons = Frame()
        self.frm_buttons.pack(fill=X, ipadx=5, ipady=5)

        self.btn_submit = Button(master=self.frm_buttons, text="Добавить", command=self.getText)
        self.btn_submit.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_clear = Button(master=self.frm_buttons, text="Отчистить", command=self.deleteText)
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_nw = Button(master=self.frm_buttons, text="New", command=self.create_new_win)
        self.btn_nw.pack(side=LEFT, padx=10, ipadx=10)

        self.mainText = Text(self.root)
        self.mainText.pack()

        self.scroll = Scrollbar(command=self.mainText.yview)
        self.scroll.pack(side=LEFT, fill=Y)

        self.mainText.config(yscrollcommand=self.scroll.set)

        self.label = Label()
        self.label.pack(side=LEFT)




    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.pack(anchor=CENTER)
        #self.menubar

    def create_new_win(self, width, height, title="Генератор", resizable=(False, False), icon=None):
        SecondWindow(self.root, width, height, title, resizable, icon)

    def getText(self):
        self.prepod_get = self.entry.get()
        self.discip_get = self.combobox_discip.get()
        self.type_ed_prog_get = self.combobox_ed_prog.get()
        self.doc = DocxTemplate("RPD_test.docx")
        self.context = {'prepod': self.prepod_get, 'discip': self.discip_get, 'type_ed_prog': self.type_ed_prog_get}
        self.doc.render(self.context)
        self.doc.save("RPD_final.docx")
        self.document = dc.Document("RPD_final.docx")
        self.fullText = []
        for para in self.document.paragraphs:
            self.fullText.append(para.text)
        mb.showinfo("Внимание", "Титульный лист сформирован")
        self.mainText.insert('1.0', self.fullText)

    def deleteText(self):
        self.entry.delete(0, END)

if __name__ == "__main__":
    window = MainWindow(600, 600, "Tkinter")

    window.create_new_win(600, 600)
    window.run()
