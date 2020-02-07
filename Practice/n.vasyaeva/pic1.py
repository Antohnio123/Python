import tkinter



width = 350
height = 250
title = "vasyaeva"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off


# Написать свой код сюда ----------------------

points = [10, 180, 200, 180, 160, 220, 40, 220]
canvas.create_polygon(points, outline='black',
    fill='grey', width=1)

canvas.create_line(70, 180, 40, 40, fill='brown', width=2)

points = [70, 180, 150, 150, 170, 120, 160, 70, 120, 50, 40, 40, 90, 80, 100, 120, 90, 150, 70, 180]
canvas.create_polygon(points, outline='black',
    fill='red', width=1)

canvas.create_line(40, 40, 30, 30, fill='brown', width=2)

points = [30, 30, 60, 20, 20, 10]
canvas.create_polygon(points, outline='black',
    fill='blue', width=1)

canvas.create_oval(260, 10, 300, 50, outline="yellow",
        fill="yellow", width=1)

canvas.create_line(250, 20, 220, 20, fill='yellow')
canvas.create_line(250, 30, 220, 40, fill='yellow')
canvas.create_line(260, 40, 230, 60, fill='yellow')
canvas.create_line(270, 50, 250, 80, fill='yellow')
canvas.create_line(280, 50, 280, 90, fill='yellow')

x = 0
y = 0
n = 100

canvas.create_rectangle(x, y, width, height)


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()

