import tkinter

width = 500
height = 400
title = "Pirating"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
# Написать свой код сюда ----------------------
x = 0
y = 1
n = 100
#canvas.create_rectangle(x, y, width, height)
#canvas.create_line(15, 25, 200, 25, fill="#fb0")
#canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
canvas.create_oval(70, 70, 100, 100, fill="#ff0", width=2)
canvas.create_line(85, 100, 85, 200, fill="#0f0", width=2)
canvas.create_line(55, 55, 75, 75, fill="#f00", width=2)
canvas.create_line(55, 90, 70, 90, fill="#f00", width=2)
canvas.create_line(100, 90, 120, 90, fill="#f00", width=2)
canvas.create_line(120, 55, 95, 75, fill="#f00", width=2)
canvas.create_arc(85, 150, 100, 180, start=0, extent=270, fill="#3f3", width=2)
#=Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))


#text = Text(width=25, height=5, bg="darkgreen", fg='white', wrap=WORD)
#text.pack()




# Рисуем красные линии
#for i in range(n):
#    y_add = (i / (n - 1)) * (height - 1)
#    canvas.create_line(x, y, x + width - 1, y + y_add, fill='red')

# Рисуем зеленые линии
#for i in range(n):
#    y_add = (i / (n - 1)) * (height - 1)
#    x_add = (i / (n - 1)) * (width - 1)
#    pass
    # Зеленые линии
#    canvas.create_line(x, y + y_add, x + x_add, y + height - 1, fill='green')

# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()