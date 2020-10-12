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
        img = PilImage.open('addimg.png')
        img = img.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        if icon:
            self.root.iconbitmap(icon)

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

    def get_text(self):
        text_get = self.text_edit.get("1.0", END)
        doc = DocxTemplate("RPD2.docx")
        context = {'mesto_discip': text_get}
        doc.render(context)
        doc.save("RPD2.docx")
        document = dc.Document("RPD2.docx")
        full_text = []
        for para in document.paragraphs:
            full_text.append(para.text)
        mb.showinfo("Внимание", "Титульный лист сформирован")
        # self.mainText.insert('1.0', full_text)

    def delete_text(self):
        self.text_edit.delete(1.0, END)
