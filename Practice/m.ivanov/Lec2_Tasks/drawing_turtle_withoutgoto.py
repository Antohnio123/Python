import turtle
import math

turtle.title ("Run, turtle, run")

width = 500
height = 400

x = -width/2
y = height/2
n = 100

turtle.setup = (width + 10, height + 10)
turtle.speed (10)
turtle.radians ()
turtle.penup ()
turtle.goto (x,y)
turtle.pendown()

# Рисуем красные линии
turtle.color('red')
for i in range(n):
    y_add = (i / (n - 1)) * height
    l = math.sqrt ((width)**2 + y_add**2)
    a = math.asin (y_add/l)
    turtle.right (a)
    turtle.forward (l)
    turtle.penup ()
    turtle.back (l)
    turtle.left (a)
    turtle.pendown ()

# Рисуем зелёные линии
turtle.color('green')
y_prev = 0
for i in range(n):
    x_add = (i / (n - 1)) * width
    y_add = (i / (n - 1)) * height
    turtle.penup ()
    turtle.right (math.pi/2)
    turtle.forward (y_add - y_prev)
    turtle.left (math.pi/2)
    turtle.pendown ()
    l = math.sqrt (x_add**2 + ((height - y_add)**2))
    a = math.asin ((height - y_add)/l)
    turtle.right (a)
    turtle.forward (l)
    turtle.penup ()
    turtle.back (l)
    turtle.pendown ()
    turtle.left (a)
    y_prev = y_add

turtle.mainloop()