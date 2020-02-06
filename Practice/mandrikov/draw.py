import tkinter
import math

width = 500
height = 400
title = "mandrikov"

top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2, bg='green')
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

# Написать свой код сюда ---------------------
canvas.create_rectangle(0, 300, 500, 0, fill='blue', outline='blue')
canvas.create_oval(50, 50, 100, 100, fill='yellow', outline='yellow')
canvas.create_rectangle(400, 400, 300, 350, fill='gray')
canvas.create_polygon(300, 350, 350, 325, 400, 350)
canvas.create_rectangle(370, 400, 330, 370, fill='black')

x = 60
y = 60
n = 10
p = 350
for i in range(n, 300, 10):
    y_add = p / (2 * math.pi)
    canvas.create_line(x, y, x + y_add - 100, y + y_add - 100, fill='yellow')
#Почему цикл не сработал?

# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()
