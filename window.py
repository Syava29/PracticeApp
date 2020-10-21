from tkinter import *
from tkinter import Tk, Text, END, filedialog
from tkinter import messagebox as mb
from tkinter import ttk
import time, threading
from tkinter.ttk import Frame, Button
from PIL import Image as PilImage
from PIL import ImageTk
from tkinter.scrolledtext import ScrolledText
import sqlite3
import os

import docx as dc
from docxtpl import DocxTemplate

from second_window import SecondWindow
from window3 import Window3
from window4 import Window4
from window5 import Window5


class MainWindow:
    def __init__(self, width, height, title, resizable=(False, False),
                 icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.root.config(bg="#1f4b99")

        self.root.iconbitmap('images/osu2.ico')

        img = PilImage.open('images/add_png.png')
        img = img.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        img2 = PilImage.open('images/download_png.png')
        img2 = img2.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image2 = ImageTk.PhotoImage(img2)

        img3 = PilImage.open('images/help_png.png')
        img3 = img3.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image3 = ImageTk.PhotoImage(img3)

        self.data_file = open("data/data1.txt", "w+")
        self.text_data = self.data_file.read()
        self.data_file.close()

        # connect к БД
        self.conn = sqlite3.connect('data/db_data.db')
        self.cur = self.conn.cursor()

        self.counter1 = 0

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.fileMenu = Menu(self.menubar)
        self.fileMenu.add_command(label="Открыть файл", command=self.on_open)

        menubar_label = [
            "Цели и задачи освоения дисциплины",
            "Место дисциплины в структуре ОП",
            "Планируемые результаты обучения по дисциплине",
            "Структура дисциплины и распределение её трудоёмкости"
        ]

        description_menu_bar = Menu(self.menubar)
        description_menu_bar.add_command(label=menubar_label[0], command=lambda: self.create_new_win(
            600, 600))
        description_menu_bar.add_command(label=menubar_label[1], command=lambda: self.create_new_win2(
            600, 600))
        description_menu_bar.add_command(label=menubar_label[2], command=lambda: self.create_new_win4(
            600, 600))
        description_menu_bar.add_command(label=menubar_label[3], command=lambda: self.create_new_win5(
            600, 600))

        self.menubar.add_cascade(label="Файл", menu=self.fileMenu)
        self.menubar.add_cascade(label="Содержание РПД", menu=description_menu_bar)

        self.frm_form = LabelFrame(relief=SUNKEN, borderwidth=3, text="Титульный лист")
        self.frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)

        self.labels = [
            "ФИО:",
            "Дисциплина: *",
            "Тип образовательной программы: *",
            "Форма обучения: *",
            "Направление подготовки: *",
            "Профиль: *",
            "Инфститут(факультет)",
            "Кафедра"
        ]

        # Создает ярлык с текстом из списка ярлыков.
        self.label = Label(self.frm_form, text=self.labels[0])
        self.label_1 = Label(self.frm_form, text=self.labels[1])
        self.label_2 = Label(self.frm_form, text=self.labels[2])
        self.label_3 = Label(self.frm_form, text=self.labels[3])
        self.label_4 = Label(self.frm_form, text=self.labels[4])
        self.label_5 = Label(self.frm_form, text=self.labels[5])
        self.label_inst_fac = Label(self.frm_form, text=self.labels[6])
        self.label_kaf = Label(self.frm_form, text=self.labels[7])
        # Создает текстовое поле которая соответствует ярлыку.
        self.combobox_inst_fac = ttk.Combobox(self.frm_form, width=50, values=[
            "Физико-математический факультет",
            "Институт естественных наук и биотехнологии",
            "Юридический институт",
            "Институт приборостроения, автоматизации и информационных технологий"], )

        self.combobox_kaf = ttk.Combobox(self.frm_form, width=50, values=[
            "Кафедра алгебры и математических методов в экономике",
            "Кафедра геометрии и методики преподавания математики",
            "Кафедра информатики",
            "Кафедра математики и прикладных информационных технологий имени Н.А. Ильиной",
            "Кафедра математического анализа и дифференциальных уравнений",
            "Кафедра экспериментальной и теоретической физики"])

        self.entry = Entry(self.frm_form, width=50)
        # entry_1 = Entry(master=frm_form, width=50)
        # entry_2 = Entry(master=frm_form, width=50)
        # entry_3 = Entry(master=frm_form, width=50)
        # self.entry_4 = Entry(self.frm_form, width=50)
        # self.entry_5 = Entry(self.frm_form, width=50)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        self.label.grid(row=1, column=0, sticky="e")
        self.label_inst_fac.grid(row=2, column=0, sticky="e")
        self.label_kaf.grid(row=3, column=0, sticky="e")
        self.label_1.grid(row=4, column=0, sticky="e")
        self.label_2.grid(row=5, column=0, sticky="e")
        self.label_3.grid(row=6, column=0, sticky="e")
        self.label_4.grid(row=7, column=0, sticky="e")
        self.label_5.grid(row=8, column=0, sticky="e")

        self.entry.grid(row=1, column=1, pady=10)
        self.combobox_inst_fac.grid(row=2, column=1, pady=10)
        self.combobox_kaf.grid(row=3, column=1, pady=10)

        self.button_authorization = Button(self.frm_form, text='Вход', width=5, command=self.authorization).grid(row=1,
                                                                                                                 column=3)

        self.combobox_discip = ttk.Combobox(self.frm_form, width=50, values=[
            "Программирование",
            "Философия",
            "Эконометрика",
            "Иностранный язык"])
        self.combobox_discip.grid(row=4, column=1, pady=10)

        self.combobox_ed_prog = ttk.Combobox(self.frm_form, width=50, values=[
            "бакалавриат",
            "специалитет, магистратура"])
        self.combobox_ed_prog.grid(row=5, column=1, pady=10)

        self.combobox_form_ed = ttk.Combobox(self.frm_form, width=50, values=[
            "очная",
            "очно-заочная",
            "заочная"])
        self.combobox_form_ed.grid(row=6, column=1, pady=10)

        self.combobox_naprav_podgotovki = ttk.Combobox(self.frm_form, width=50,
                                                       values=["09.03.03 Прикладная информатика"])
        self.combobox_naprav_podgotovki.grid(row=7, column=1, pady=10)

        self.combobox_profil = ttk.Combobox(self.frm_form, width=50, values=["Интеллектуальная обработка данных"])
        self.combobox_profil.grid(row=8, column=1, pady=10)

        # основные кнопки
        self.frm_buttons = Frame()
        self.frm_buttons.pack(fill=X, ipadx=5, ipady=5)

        self.btn_submit = Button(self.frm_buttons, text="Добавить", image=self.photo_image, compound=LEFT,
                                 command=lambda: self.get_text())
        self.btn_submit.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_clear = Button(self.frm_buttons, text="Отчистить", command=self.delete_text())
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_help = Button(self.frm_buttons, image=self.photo_image3, command=self.help_mb)
        self.btn_help.pack(side=LEFT, padx=10, ipadx=10)

        # Progressbar
        # self.pb = ttk.Progressbar(self.frm_buttons, mode="determinate", maximum=100, value=0)
        # self.pb.pack()

        # Добавленные рабочие программы

        self.frm_form2 = LabelFrame(relief=SUNKEN, borderwidth=3, text="Добавленные рабочие программы")
        self.frm_form2.pack(fill=X, ipadx=30, ipady=30, padx=10)

        self.label_add_programm1 = Label(self.frm_form2, text='■').grid(row=1, column=0)
        self.label_add_programm2 = Label(self.frm_form2, text='■').grid(row=2, column=0)
        self.label_add_programm3 = Label(self.frm_form2, text='■').grid(row=3, column=0)
        self.label_add_programm4 = Label(self.frm_form2, text='■').grid(row=4, column=0)

        self.entry_add_programm1 = Entry(self.frm_form2, width=50)
        self.entry_add_programm1.grid(row=1, column=1, pady=10, padx=10)
        self.entry_add_programm2 = Entry(self.frm_form2, width=50)
        self.entry_add_programm2.grid(row=2, column=1, pady=10, padx=10)
        self.entry_add_programm3 = Entry(self.frm_form2, width=50)
        self.entry_add_programm3.grid(row=3, column=1, pady=10, padx=10)
        self.entry_add_programm4 = Entry(self.frm_form2, width=50)
        self.entry_add_programm4.grid(row=4, column=1, pady=10, padx=10)

        self.btn_add_programm1 = Button(self.frm_form2, image=self.photo_image2, command=self.open_word_file).grid(
            row=1, column=2)
        self.btn_add_programm2 = Button(self.frm_form2, image=self.photo_image2).grid(row=2, column=2)
        self.btn_add_programm3 = Button(self.frm_form2, image=self.photo_image2).grid(row=3, column=2)
        self.btn_add_programm4 = Button(self.frm_form2, image=self.photo_image2).grid(row=4, column=2)
        # основной текст

        # self.mainText = ScrolledText(self.root, relief=SUNKEN, bd=5, font=("Times New Roman", 11), wrap=WORD)
        # self.mainText.pack()

        # self.scroll = Scrollbar(command=self.mainText.yview)
        # self.scroll.pack(side=LEFT, fill=Y)

        # self.mainText.config(yscrollcommand=self.scroll.set)

        self.label = Label()
        self.label.pack(side=LEFT)

        self.entry_add_programm1.insert(0, self.text_data)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.pack(anchor=CENTER)
        # self.menubar

    def create_new_win(self, width, height, title="Генератор рабочей программы дисциплины", resizable=(False, False),
                       icon=None):
        SecondWindow(self.root, width, height, title, resizable, icon)

    def create_new_win2(self, width, height, title="Генератор рабочей программы дисциплины", resizable=(False, False),
                        icon=None):
        Window3(self.root, width, height, title, resizable, icon)

    def create_new_win4(self, width, height, title="Генератор рабочей программы дисциплины", resizable=(False, False),
                        icon=None):
        Window4(self.root, width, height, title, resizable, icon)

    def create_new_win5(self, width, height, title="Генератор рабочей программы дисциплины", resizable=(False, False),
                        icon=None):
        Window5(self.root, width, height, title, resizable, icon)

    def on_open(self):
        ftypes = [('py файлы', '*.py'), ('Все файлы', '*')]
        dlg = filedialog.Open(self.root, filetypes=ftypes)
        fl = dlg.show()
        fll = open(fl)
        fl2 = fll.readline()
        self.mainText.insert(1.0, fl2)

    def get_text(self):
        prepod_get = self.entry.get()
        discip_get = self.combobox_discip.get()
        stype_ed_prog_get = self.combobox_ed_prog.get()
        form_ed = self.combobox_form_ed.get()
        naprav_podgotovki = self.combobox_naprav_podgotovki.get()
        profil = self.combobox_profil.get()
        inst_fac = self.combobox_inst_fac.get()
        kaf = self.combobox_kaf.get()
        doc = DocxTemplate("data/RPD_test.docx")
        context = {'prepod': prepod_get, 'discip': discip_get, 'type_ed_prog': stype_ed_prog_get, 'form_ed': form_ed,
                   'profil': profil, 'naprav_podgotovki': naprav_podgotovki, 'inst_fac': inst_fac,
                   'kafedra': kaf, 'mesto_discip': "{{mesto_discip}}", 'task': "{{task}}",
                   'target': "{{target}}", 'description1': "{{description1}}", 'kod_komp1': "{{kod_komp1}}",
                   'description2': "{{description2}}", 'kod_komp2': "{{kod_komp2}}",
                   'zuv1_1': "{{zuv1_1}}", 'zuv1_2': "{{zuv1_2}}", 'zuv1_3': "{{zuv1_3}}",
                   'zuv2_1': "{{zuv2_1}}", 'zuv2_2': "{{zuv2_2}}", 'zuv2_3': "{{zuv2_3}}"
                   }
        doc.render(context)
        doc.save("data/RPD1.docx")

        data_file = open("data/data1.txt", "w+")
        str1 = data_file.read()
        str1 = str1 + discip_get
        data_file.write(str1)
        data_file.close()

        if self.counter1 == 0:
            self.entry_add_programm1.insert(0, str1)
        if self.counter1 == 1:
            self.entry_add_programm2.insert(0, str1)
        if self.counter1 == 2:
            self.entry_add_programm3.insert(0, str1)
        if self.counter1 == 3:
            self.entry_add_programm4.insert(0, str1)

        self.counter1 += 1

        mb.showinfo("Внимание", "Титульный лист сформирован")
        # self.mainText.insert('1.0', full_text)

    def delete_text(self):
        self.entry.delete(0, END)

    def help_mb(self):
        mb.showinfo("Помощь", "Укажите год набора, направление подготовки, профиль и наименование дисциплины. "
                              "Ниже показаны все добавленные вами рабочие программы")

    def open_word_file(self):
        os.startfile(r'готовые программы\рабочая программа.docx')

    def authorization(self):
        i = 0
        k = 0
        flag = False
        input_text = self.entry.get()

        self.cur.execute(f'SELECT fio_prepod FROM prepod')
        all_results2 = self.cur.fetchall()

        while k < len(all_results2):
            string_test = all_results2[k]

            if input_text == string_test[0]:
                self.entry.delete(0, END)
                self.entry.insert(0, string_test[0])

                self.cur.execute(f'SELECT discip FROM discip WHERE id_prepod == {k + 1}')
                all_results = self.cur.fetchall()

                while i < len(all_results):
                    self.combobox_discip["values"] = all_results
                    i += 1
                mb.showinfo("Успешно", "Вход выполнен успешно")
                flag = True

            k += 1
        if not flag:
            mb.showerror('Вход не выполнен', 'Такого преподавателя нет')

        self.cur.execute(f'SELECT discip FROM discip WHERE id_prepod == {4}')
        all_results = self.cur.fetchall()

        while i < len(all_results):
            self.combobox_discip["values"] = all_results
            i += 1
        self.combobox_profil.insert(0, len(all_results))


if __name__ == "__main__":
    window = MainWindow(600, 600, "Генератор рабочей программы дисциплины")
    window.run()
