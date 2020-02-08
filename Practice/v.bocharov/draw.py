import tkinter

width = 500
height = 400
title = "bocharov"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off


# Написать свой код сюда ----------------------

canvas.create_rectangle(0,300,500,400,fill="green",outline="green")
canvas.create_rectangle(0,0,500,300,fill="lightblue",outline="lightblue")
canvas.create_rectangle(100,275,300,325,fill="yellow",outline="yellow")
canvas.create_rectangle(150,235,250,300,fill="yellow",outline="yellow")
canvas.create_rectangle(155,237,245,275,fill="blue",outline="blue")
canvas.create_rectangle(197,235,202,275,fill="yellow",outline="yellow")
canvas.create_oval(130,300,180,350,fill="black",outline="black")
canvas.create_oval(220,300,270,350,fill="black",outline="black")


# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()
