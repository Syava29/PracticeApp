from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button
from PIL import Image as PilImage
from PIL import ImageTk
from docxtpl import DocxTemplate
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
import docx as dc

from collections import Counter
from openpyxl import load_workbook
import re


class Window4:
    def __init__(self, parent, width, height, title="Генератор Рабочей программы дисциплины", resizable=(False, False),
                 icon=r"main.ico"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.root.config(bg="#1f4b99")

        img = PilImage.open('images/add_png.png')
        img = img.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        img3 = PilImage.open('images/help_png.png')
        img3 = img3.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image3 = ImageTk.PhotoImage(img3)

        self.root.iconbitmap('images/osu2.ico')

        self.frm_form = LabelFrame(self.root, relief=SUNKEN, borderwidth=3, text="Планируемые результаты обучения")
        self.frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)

        self.label_text1 = Label(self.frm_form,
                                 text=
                                 "Добавьте несколько компетенций с помощью кнопки 'Добавить'"
                                 " и сохраните изменения").pack()
        self.label_text = Label(self.frm_form, text="Код компетенции").pack()

        self.combobox = ttk.Combobox(self.frm_form, values=[
            'УК-1',
            'УК-2',
            'УК-3',
            'УК-4',
            'УК-5'])
        self.combobox.pack()

        self.frm_buttons = Frame(self.root)
        self.frm_buttons.pack(fill=X, ipadx=5, ipady=5)

        self.btn_submit = Button(self.frm_buttons, text="Добавить", image=self.photo_image, compound=LEFT,
                                 command=self.add_zuv)
        self.btn_submit.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_clear = Button(self.frm_buttons, text="Сохранить", command=self.save_zuv)
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_help = Button(self.frm_buttons, image=self.photo_image3)
        self.btn_help.pack(side=LEFT, padx=10, ipadx=10)

        self.f_top = Frame(self.frm_form)  # frame для текста
        self.f_mid = Frame(self.frm_form)
        self.f_bot = Frame(self.frm_form)

        self.text_edit = ScrolledText(self.f_top, width=5, height=1, font=("Times New Roman", 11), wrap=WORD)
        self.label_text = Label(self.frm_form, text="Описание компетенции").pack()
        self.text_edit2 = ScrolledText(self.f_top, width=45, height=10, font=("Times New Roman", 11), wrap=WORD)
        self.text_edit3 = ScrolledText(self.f_mid, width=5, height=1, font=("Times New Roman", 11), wrap=WORD)
        self.text_edit4 = ScrolledText(self.f_mid, width=45, height=10, font=("Times New Roman", 11), wrap=WORD)

        self.f_top.pack()
        self.f_mid.pack()

        self.text_edit.pack(side=LEFT)
        self.text_edit2.pack(side=LEFT)
        self.text_edit3.pack(side=LEFT)
        self.text_edit4.pack(side=LEFT)

        self.filename1 = "data/Компетенции.xlsx"

        self.spisok_kod = []
        self.description_zuv = []
        zuv = []

        self.add_kod_zuv_spisok = []
        self.add_zuv_spisok = []

        self.wb = load_workbook(self.filename1)
        self.sheet = self.wb['Лист1']
        self.parcing()

    def parcing(self):
        for row in self.sheet['A1':'A34']:
            string = ''
            for cell in row:
                string = string + str(cell.value)
                your_string = string
            self.spisok_kod.append(your_string)

        for row in self.sheet['B1':'B34']:
            string = ''
            for cell in row:
                string = string + str(cell.value)
                your_string = string
            self.description_zuv.append(your_string)

        # self.text_edit.insert(1.0, self.description_zuv)
        # print(self.description_zuv[0])

    def add_zuv(self):
        self.text_edit.delete(1.0, END)
        self.text_edit2.delete(1.0, END)

        self.text_edit.insert(1.0, self.combobox.get())
        self.text_edit2.insert(1.0, self.description_zuv[self.combobox.current()])
        self.text_edit3.insert(2.0, self.combobox.get())
        self.text_edit4.insert(2.0, self.description_zuv[self.combobox.current()] + '\n\n')

        self.add_kod_zuv_spisok.append(self.combobox.get())
        self.add_zuv_spisok.append(self.description_zuv[self.combobox.current()])

    def save_zuv(self):
        doc = DocxTemplate("data/RPD3.docx")

        context = {'description1': self.add_zuv_spisok[0], 'kod_komp1': self.add_kod_zuv_spisok[0],
                   'description2': self.add_zuv_spisok[1], 'kod_komp2': self.add_kod_zuv_spisok[1]}
        #context = {'description1': self.description_zuv[self.combobox.current()],
         #          'kod_komp1': self.spisok_kod[self.combobox.current()]}
        doc.render(context)
        doc.save("готовые программы/рабочая программа.docx")
        mb.showinfo("Внимание", "Планируемые результаты обучения сформированы")