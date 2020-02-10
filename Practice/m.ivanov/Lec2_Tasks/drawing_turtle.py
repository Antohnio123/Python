import turtle

turtle.title ("Run, turtle, run")

width = 500
height = 400

x = -width/2
y = height/2
n = 100

turtle.setup = (width + 10, height + 10)
turtle.speed (10)
turtle.penup()
turtle.goto (x,y)
turtle.pendown()

# Рисуем красные линии
turtle.color('red')
for i in range(n):
    y_add = (i / (n - 1)) * height
    turtle.goto (-x, y - y_add)
    turtle.penup ()
    turtle.goto (x,y)
    turtle.pendown ()

# Рисуем зелёные линии
turtle.color('green')
for i in range(n):
    x_add = (i / (n - 1)) * width
    y_add = (i / (n - 1)) * height
    turtle.goto (x + x_add, -y)
    turtle.penup ()
    turtle.goto (x, y - y_add)
    turtle.pendown ()

turtle.mainloop()