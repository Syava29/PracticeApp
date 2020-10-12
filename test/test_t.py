from tkinter import *


class MainWidow:
    def __init__(self, width, height, title="Генератор Рабочей программы дисциплины", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+300")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = MainWidow(500, 500, "TKINTER")
    window.run()