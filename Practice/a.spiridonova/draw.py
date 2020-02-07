import tkinter

width = 500
height = 400
title = "Your login"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off


# Написать свой код сюда ----------------------
def compare(a, b):
    if a >= b:
        print(str(a) +  " is bigger")
    else:
        print(str(a) + " is lower")

x = 0
y = 1
n = 100

compare(x ,y)

canvas.create_rectangle(50, 100, 450, 250, fill='red')
canvas.create_oval (100, 225, 175, 300, fill='pink')
canvas.create_oval (325, 225, 400, 300, fill='pink')
canvas.create_rectangle (100, 125, 175, 175, fill='blue')
canvas.create_rectangle (210, 125, 285, 175, fill='blue')
canvas.create_rectangle (320, 125, 395, 175, fill='blue')

# отступ слева, отступ сверху, ширина, высота

# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()


