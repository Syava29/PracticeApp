from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button
from PIL import Image as PilImage
from PIL import ImageTk
from docxtpl import DocxTemplate
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
import docx as dc


class SecondWindow:
    def __init__(self, parent, width, height, title="Генератор Рабочей программы дисциплины", resizable=(False, False),
                 icon=r"main.ico"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.root.config(bg="#1f4b99")
        if icon:
            self.root.iconbitmap(icon)

        img = PilImage.open('addimg.png')
        img = img.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        self.frm_form = LabelFrame(self.root, relief=SUNKEN, borderwidth=3, text="Цели и задачи освоения дисциплины")
        self.frm_form.pack(fill=X, ipadx=30, ipady=30, padx=10)
        self.labels = [
            "Цель освоения дисциплины:",
            "Задачи изучения дисциплины:",
            "Тип образовательной программы:",
            "Форма обучения:",
            "Направление подготовки:",
            "Профиль:",
        ]

        # Создает ярлык с текстом из списка ярлыков.
        self.label = Label(self.frm_form, text=self.labels[0])
        self.label_1 = Label(self.frm_form, text=self.labels[1])

        # Создает текстовое поле которая соответствует ярлыку.
        self.entry = Entry(self.frm_form, width=50)
        self.entry2 = Entry(self.frm_form, width=50)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        self.label.grid(row=1, column=0, sticky="e")
        self.label_1.grid(row=2, column=0, sticky="e")
        # self.entry.grid(row=1, column=1)
        # self.entry2.grid(row=2, column=1)
        self.text_edit = ScrolledText(self.frm_form, width=45, height=10, font=("Times New Roman", 11), wrap=WORD)
        self.text_edit.grid(row=1, column=1)
        self.text_edit2 = ScrolledText(self.frm_form, width=45, height=10, font=("Times New Roman", 11), wrap=WORD)
        self.text_edit2.grid(row=2, column=1)
        # self.grab_focis()

        self.frm_buttons = Frame(self.root)
        self.frm_buttons.pack(fill=X, ipadx=5, ipady=5)

        self.btn_submit = Button(self.frm_buttons, text="Добавить", image=self.photo_image, compound=LEFT,
                                 command=self.get_text)
        self.btn_submit.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_clear = Button(self.frm_buttons, text="Отчистить")
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

    def get_text(self):
        text_get = self.text_edit.get("1.0", END)
        text_get2 = self.text_edit2.get("1.0", END)
        # discip_get = self.combobox_discip.get()
        # stype_ed_prog_get = self.combobox_ed_prog.get()
        doc = DocxTemplate("RPD1.docx")
        context = {'target': text_get, 'task': text_get2, 'mesto_discip': "{{mesto_discip}}"}
        doc.render(context)
        doc.save("RPD2.docx")
        document = dc.Document("RPD2.docx")
        full_text = []
        for para in document.paragraphs:
            full_text.append(para.text)
        mb.showinfo("Внимание", "Титульный лист сформирован")
        # self.mainText.insert('1.0', full_text)

    # Фокусировка окна
    # def grab_focis(self):
    # self.root.grab_set()
    # self.root.focus_set()
    # self.root.wait_window()
