from tkinter import *
from tkinter import Tk, Text, END, filedialog
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.ttk import Frame, Button
from PIL import Image as PilImage
from PIL import ImageTk
from tkinter.scrolledtext import ScrolledText

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
        if icon:
            self.root.iconbitmap(icon)

        img = PilImage.open('addimg.png')
        img = img.resize((18, 18), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

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
            "Дисциплина:",
            "Тип образовательной программы:",
            "Форма обучения:",
            "Направление подготовки:",
            "Профиль:",
        ]

        # Создает ярлык с текстом из списка ярлыков.
        self.label = Label(self.frm_form, text=self.labels[0])
        self.label_1 = Label(self.frm_form, text=self.labels[1])
        self.label_2 = Label(self.frm_form, text=self.labels[2])
        self.label_3 = Label(self.frm_form, text=self.labels[3])
        self.label_4 = Label(self.frm_form, text=self.labels[4])
        self.label_5 = Label(self.frm_form, text=self.labels[5])

        # Создает текстовое поле которая соответствует ярлыку.
        self.entry = Entry(self.frm_form, width=50)
        # entry_1 = Entry(master=frm_form, width=50)
        # entry_2 = Entry(master=frm_form, width=50)
        # entry_3 = Entry(master=frm_form, width=50)
        # self.entry_4 = Entry(self.frm_form, width=50)
        # self.entry_5 = Entry(self.frm_form, width=50)
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
        # self.entry_4.grid(row=5, column=1)
        # self.entry_5.grid(row=6, column=1)

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

        self.combobox_naprav_podgotovki = ttk.Combobox(self.frm_form, values=["09.03.03 Прикладная информатика"])
        self.combobox_naprav_podgotovki.grid(row=5, column=1)

        self.combobox_profil = ttk.Combobox(self.frm_form, values=["Интеллектуальная обработка данных"])
        self.combobox_profil.grid(row=6, column=1)

        self.frm_buttons = Frame()
        self.frm_buttons.pack(fill=X, ipadx=5, ipady=5)

        self.btn_submit = Button(self.frm_buttons, text="Добавить", image=self.photo_image, compound=LEFT,
                                 command=lambda: self.get_text())
        self.btn_submit.pack(side=LEFT, padx=10, ipadx=10)

        self.btn_clear = Button(self.frm_buttons, text="Отчистить", command=self.delete_text())
        self.btn_clear.pack(side=LEFT, padx=10, ipadx=10)

        self.mainText = ScrolledText(self.root, relief=SUNKEN, bd=5, font=("Times New Roman", 11), wrap=WORD)
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
        # self.menubar

    def create_new_win(self, width, height, title="Генератор", resizable=(False, False), icon=None):
        SecondWindow(self.root, width, height, title, resizable, icon)

    def create_new_win2(self, width, height, title="Генератор", resizable=(False, False), icon=None):
        Window3(self.root, width, height, title, resizable, icon)

    def create_new_win4(self, width, height, title="Генератор", resizable=(False, False), icon=None):
        Window4(self.root, width, height, title, resizable, icon)

    def create_new_win5(self, width, height, title="Генератор", resizable=(False, False), icon=None):
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

        doc = DocxTemplate("RPD_test.docx")
        context = {'prepod': prepod_get, 'discip': discip_get, 'type_ed_prog': stype_ed_prog_get, 'form_ed': form_ed,
                   'profil': profil, 'naprav_podgotovki': naprav_podgotovki, 'mesto_discip': "{{mesto_discip}}", 'task': "{{task}}",
                   'target': "{{target}}", 'description1': "{{description1}}", 'kod_komp1': "{{kod_komp1}}",
                   'description2': "{{description2}}", 'kod_komp2': "{{kod_komp2}}"}
        doc.render(context)
        doc.save("RPD1.docx")
        document = dc.Document("RPD1.docx")
        full_text = []
        for para in document.paragraphs:
            full_text.append(para.text)
        mb.showinfo("Внимание", "Титульный лист сформирован")
        self.mainText.insert('1.0', full_text)

    def delete_text(self):
        self.entry.delete(0, END)


if __name__ == "__main__":
    window = MainWindow(600, 600, "Генератор рабочей программы дисциплины")
    window.run()
