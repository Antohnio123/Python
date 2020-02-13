from tkinter import *

title = "Привет"

root = Tk()
if title:
    root.title(title)
b = Button(text="Кнопка не работает")
c = Canvas(root, width=300, height=400, bg='white')

c.create_polygon((100, 250), (200, 250), (200, 150), (215, 150), (150, 85), (85, 150), (100, 150), fill='lightblue')

c.create_oval(190, 40, 240, 90, fill='orange', outline='yellow')

for x in range(50, 251, 10):
    c.create_arc(0 + x, 225, 100 + x, 325, fill='green', start=135, extent=45, style=ARC)

b.pack()
c.pack()

root.mainloop()