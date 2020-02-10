import tkinter
import math

width = 500 # габариты окна
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
canvas.create_rectangle(0, 300, 500, 0, fill='blue', outline='blue') # создаем небо
canvas.create_oval(50, 50, 100, 100, fill='yellow', outline='yellow') # создаем солнце
canvas.create_rectangle(400, 400, 300, 350, fill='gray') # создаем дом
canvas.create_polygon(300, 350, 350, 325, 400, 350) # создаем крышу дома
canvas.create_rectangle(370, 400, 330, 370, fill='black') # ворота для дома

x = 80
y = 80
n = 45
p = 350
for i in range(0,360, 10): #создание лучей для солнца
    print(i)
    x_add = 60 * math.cos(i)
    y_add = 60 * math.sin(i)
    canvas.create_line(x, y, x + x_add, y + y_add, fill='yellow')

# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()
