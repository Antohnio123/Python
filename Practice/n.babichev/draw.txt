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
        print(str(a) +  " is begger")
    else:
        print(str(a) + " is lowwer")

x = 0
y = 1
n = 100

compare(x ,y)

canvas.create_rectangle(x, y, width, height)

# Рисуем красные линии
for i in range(n):
    y_add = (i / (n - 1)) * (height - 1)
    canvas.create_line(x, y, x + width - 1, y + y_add, fill='red')

# Рисуем зеленые линии
for i in range(n):
    y_add = (i / (n - 1)) * (height - 1)
    x_add = (i / (n - 1)) * (width - 1)
    pass
    # Зеленые линии
    canvas.create_line(x, y + y_add, x + x_add, y + height - 1, fill='green')

# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()


