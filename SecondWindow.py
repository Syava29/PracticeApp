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
        self.root.title("Генератор")
        self.root.geometry("600x600")

    def labb(self):
        Label(self.root, text='131313').pack




if __name__ == "__main__":
    window = SecondWin(500, 500, "TKINTER")
    window.run()
    SecondWin.create_menu()
    SecondWin.labb()