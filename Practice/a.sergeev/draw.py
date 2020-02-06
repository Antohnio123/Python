import tkinter

width = 500
height = 500
title = "Your panzer"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off


# Напсать свой код сюда ----------------------
def compare(a, b):
    if a >= b:
        print(str(a) +  " is begger")
    else:
        print(str(a) + " is lowwer")

x = 0
y = 1
n = 100

compare(x ,y)

canvas.create_rectangle(25, 275, 475, 345, width=2, fill='orange')
canvas.create_rectangle(150, 225, 350, 275,width=2, fill='pink')
canvas.create_rectangle(225, 175, 325, 225, width=2, fill='green')
canvas.create_rectangle(50, 190, 225, 210, width=2, fill='blue')
canvas.create_oval (25, 25,100, 100, fill='yellow')
canvas.create_oval (25, 325,75, 375, fill='black')
canvas.create_oval (75, 325,125, 375, fill='black')
canvas.create_oval (125, 325,175, 375, fill='black')
canvas.create_oval (175, 325,225, 375, fill='black')
canvas.create_oval (225, 325,275, 375, fill='black')
canvas.create_oval (275, 325,325, 375, fill='black')
canvas.create_oval (325, 325,375, 375, fill='black')
canvas.create_oval (375, 325,425, 375, fill='black')
canvas.create_oval (425, 325,475, 375, fill='black')




# Рисуем красные линии
#for i in range(n):
    #y_add = (i / (n - 1)) * (height - 1)
    #canvas.create_line(x, y, x + width - 1, y + y_add, fill='red')

# Рисуем зеленые линии
#for i in range(n):
    #y_add = (i / (n - 1)) * (height - 1)
    #x_add = (i / (n - 1)) * (width - 1)
    #pass
     #Зеленые линии
    #canvas.create_line(x, y + y_add, x + x_add, y + height - 1, fill='green')

# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()
