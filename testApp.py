from docxtpl import DocxTemplate
from tkinter import *
from tkinter import scrolledtext


""" Бизнес_логика приложения"""
def clicked():
    doc = DocxTemplate("RPD_test.docx")
    context = {'prepod': "ФИО"}
    doc.render(context)
    doc.save("RPD_final.docx")




""" Визуализация """

window = Tk()
window.title("Генератор Рабочей программы дисциплины")
window.geometry('1500x500')

text_box = Text()
text_box.grid(column=1, row=1)

btn = Button(window, text="Подобрать литературу", comand=clicked())
btn.grid(column=8, row=7)



window.mainloop()

