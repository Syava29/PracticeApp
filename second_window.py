from tkinter import *


class SecondWindow:
    def __init__(self, parent, width, height, title="Генератор Рабочей программы дисциплины", resizable=(False, False),
                 icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.grab_focis()


    # Фокусировка окна
    def grab_focis(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
