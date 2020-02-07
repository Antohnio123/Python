from tkinter import *
import turtle
#import math

def clicked():
    ellipse()

def ellipse():
    turtle.reset()
    turtle.up()
    turtle.goto(-50, -100)
    turtle.color("lime")
    turtle.width(5)
    turtle.down()
    turtle.right(180)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()
    turtle.color("black")

    turtle.right(135)
    turtle.forward(120)
    turtle.right(-45)
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(-135)
    turtle.forward(120)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(135)
    turtle.forward(120)
    turtle.right(45)
    turtle.forward(200)
    turtle.end_fill()
    turtle.right(135)
    turtle.forward(120)
    turtle.right(-45)
    turtle.forward(200)
    turtle.up()
    turtle.goto(-200, 0)
    turtle.color("blue")
    turtle.width(2)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.right(-90)
    turtle.forward(20)
    turtle.mainloop()

window = Tk()
window.title("Рисовалка")
window.geometry("250x100")
lbl_tree = Label(window, text="Кубик", font=("Consolas", 12, "bold"), padx=10, pady=10)
lbl_tree.grid(column=0, row=0)
btn = Button(window, text="Нарисовать", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()