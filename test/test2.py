import tkinter as Tk

root = Tk.Tk()
root.geometry('300x300')


def resize_it(event):
    frame.configure(width=event.width / 3, height=event.height / 2)
    frame1.configure(width=event.width / 3 * 2, height=event.height / 2)
    root.configure(width=event.width, height=event.height)


frame = Tk.Frame(root, bg='red')
frame.pack(side='left', expand=True, fill=Tk.BOTH)
frame.grid_propagate(0)

frame1 = Tk.Frame(root, bg='blue')
frame1.pack(side='left', expand=True, fill=Tk.BOTH)
frame1.grid_propagate(0)

root.bind('<Configure>', resize_it)
root.mainloop()
