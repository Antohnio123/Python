import tkinter



width = 640
height = 480
title = "MyFirstPicture"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off


# Написать свой код сюда ----------------------
canvas.create_rectangle(10, 10, 90, 120,
    outline='black', fill="blue")

points = [20, 20, 80, 20, 80, 30, 30, 30, 30, 60, 60, 60,
          60, 70, 30, 70, 30, 110, 20, 110, 20, 20]
canvas.create_polygon(points, outline='black',
    fill='red', width=3)

canvas.create_oval(140, 60, 240, 170, outline="green",
        fill="yellow", width=5)

canvas.create_oval(170, 90, 210, 140, outline="green",
        fill="white", width=5)

x = 0
y = 0
n = 100

if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()
