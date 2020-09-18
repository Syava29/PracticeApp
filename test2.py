from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Окно для выбора файла")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Открыть", command=self.onOpen)
        menubar.add_cascade(label="Файл", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [('Python файлы', '*.py'), ('Все файлы', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):
        with open(filename, "r") as f:
            text = f.read()

        return text


def main():
    root = Tk()
    ex = Example()
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()