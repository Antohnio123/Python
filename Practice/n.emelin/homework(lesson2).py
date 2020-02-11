from random import *
from tkinter import *
size = 400
root = Tk()
root.title("Домашнее задание/n.emelin")      #
canvas = Canvas(root, width=size, height=size)
canvas.pack()
def pictures (self):
    while True:
      # выбор цвета
      colors = choicecolors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
               'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
      x0 = randint(0, size)
      y0 = randint(0, size)
      d = randint(0, size/5)
      #рисуем фигуры
      canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors )
      canvas.create_rectangle(x0, y0, x0+d, y0+d, outline=colors)
      root.update()
# кнопка
btn = Button(root,
             text="Click me",
             width=30,height=5,
             bg="white",fg="black")
btn.bind("<Button-1>", pictures)
btn.pack()
root.mainloop()