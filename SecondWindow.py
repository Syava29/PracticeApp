from tkinter import *
from tkinter import Tk, Text, Menu, END
from tkinter import ttk, filedialog
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mb
import docx as dc
from docxtpl import DocxTemplate


class SecondWin:
    def __init__(self, parent):
        self.root = Toplevel(parent)
        self.root.title("Генератор Рабочей программы дисциплины")
        self.root.geometry("600x600")

    def create_menu(self):
        menubar = Menu(self.master)
        window.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Открыть файл")
        menubar_label = [
            "Цели и задачи освоения дисциплины",
            "Место дисциплины в структуре ОП",
            "Планируемые результаты обучения по дисциплине",
            "Структура дисциплины и распределение её трудоёмкости"
        ]

        description_menu_bar = Menu(menubar)
        description_menu_bar.add_command(label="Цели и задачи освоения дисциплины")
        description_menu_bar.add_command(label=menubar_label[0])


        menubar.add_cascade(label="Файл", menu=fileMenu)
        menubar.add_cascade(label="Содержание РПД", menu=description_menu_bar)




if __name__ == "__main__":
    window = SecondWin(500, 500, "TKINTER")
    SecondWin.create_menu()
    window.run()