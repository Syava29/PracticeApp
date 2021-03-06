from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button
from PIL import Image as PilImage
from PIL import ImageTk
from docxtpl import DocxTemplate
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
import docx as dc


class Window3:
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

        self.frm_form = LabelFrame(self.root, relief=SUNKEN, borderwidth=3, text="Место дисциплины в структуре ОП")
        self.frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)
        self.text_edit = ScrolledText(self.frm_form, width=78, height=25, font=("Times New Roman", 11), wrap=WORD)
        self.text_edit.grid(row=1, column=1)

        self.frm_buttons = Frame(self.root)
        self.frm_buttons.pack(fill=X, ipadx=5, ipady=5)

        self.btn_submit = Button(self.frm_buttons, text="Добавить", image=self.photo_image, compound=LEFT,
                                 command=self.get_text)
        self.btn_submit.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_clear = Button(self.frm_buttons, text="Отчистить", command=self.delete_text)
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_help = Button(self.frm_buttons, image=self.photo_image3)
        self.btn_help.pack(side=LEFT, padx=10, ipadx=10)

    def get_text(self):
        text_get = self.text_edit.get("1.0", END)
        doc = DocxTemplate("data/RPD2.docx")
        context = {'mesto_discip': text_get, 'description1': "{{description1}}", 'kod_komp1': "{{kod_komp1}}",
                   'description2': "{{description2}}", 'kod_komp2': "{{kod_komp2}}",
                   'zuv1_1': "{{zuv1_1}}", 'zuv1_2': "{{zuv1_2}}", 'zuv1_3': "{{zuv1_3}}",
                   'zuv2_1': "{{zuv2_1}}", 'zuv2_2': "{{zuv2_2}}", 'zuv2_3': "{{zuv2_3}}"
                   }
        doc.render(context)
        doc.save("data/RPD3.docx")
        mb.showinfo("Внимание", "Титульный лист сформирован")
        # self.mainText.insert('1.0', full_text)

    def delete_text(self):
        self.text_edit.delete(1.0, END)
