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
        img = PilImage.open('addimg.png')
        img = img.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        if icon:
            self.root.iconbitmap(icon)

        self.frm_form = LabelFrame(self.root, relief=SUNKEN, borderwidth=3, text="Планируемые результаты обучения")
        self.frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)

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

        self.btn_clear = Button(self.frm_buttons, text="Отчистить", command=self.parcing)
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

        self.text_edit = ScrolledText(self.frm_form, width=45, height=10, font=("Times New Roman", 11), wrap=WORD)
        self.text_edit.pack()

        self.filename1 = "Компетенции.xlsx"

        self.spisok_kod = []
        self.description_zuv = []
        zuv = []

        self.wb = load_workbook(self.filename1)
        self.sheet = self.wb['Лист1']

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

        self.text_edit.insert(1.0, self.description_zuv)
        print(self.description_zuv[0])

    def add_zuv(self):
        doc = DocxTemplate("RPD_test.docx")
        context = {'description1': self.description_zuv[self.combobox.current()], 'kod_komp1': self.spisok_kod[self.combobox.current()]}
        doc.render(context)
        doc.save("RPD3.docx")
