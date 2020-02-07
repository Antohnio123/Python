import tkinter
import math

width = 800
height = 600
title = "Oscilloscope"


top = tkinter.Tk()
top.minsize(width=width + 10, height=height + 10)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(8, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(8, 'units')  # otherwise it's clipped off


# Написать свой код сюда ----------------------
width_screen = 500
height_screen = 500

#рисование "осциллографа"
canvas.create_rectangle (0, 0, width, height, fill='grey')
canvas.create_rectangle (50, 50, width_screen + 50, height_screen + 50, fill='black')
for i in range(9):
    canvas.create_line (50, 100 + i * 50, 550, 100 + i * 50, fill='white', dash = (10,2))
    canvas.create_line (100 + i * 50, 50, 100 + i * 50, 550, fill='white', dash = (10,2))
for i in range(4):
    canvas.create_oval (594 + 44 * i, 150, 624 + 44 * i, 180, fill='silver')
    canvas.create_oval (596 + 46 * i, 250, 616 + 46 * i, 270, fill='silver')
canvas.create_text (675,25,text = "OSCILLOSCOPE")

#ввод параметров колебаний
print ("Input amplitude ratio")
ratio = float(input())
print ("Input first frequency coefficient")
f_a= int(input())
print ("Input second frequency coefficient")
f_b = int(input())
print ("Input phase rad/pi")
phase = math.pi * float(input())

#функция находящая наибольший общий делитель и наименьшее общее кратное двух чисел
def euclide (m,n):
    l = m * n
    while m != 0 and n != 0:
        if m > n:
            m %= n
        else:
            n %= m
    return m + n, l / (m+n)

gcd, lcm = euclide (f_a, f_b)

#устранение кратности частот
f_a = f_a / gcd
f_b = f_b / gcd
lcm = lcm / gcd

#нормирование амплитуды
if ratio > 1:
    a_norm = (width_screen / 2) - 10
    b_norm = a_norm / ratio
else:
    b_norm = (height_screen / 2 ) - 10
    a_norm = b_norm * ratio

#функция, определяющая координаты кривых Лиссажу
def lissajous (x_coor,y_coor,normal_amp1,normal_amp2,frequency_ratio,phase,start_phase):
    if frequency_ratio > 1:
        x = x_coor + normal_amp1 * math.sin (frequency_ratio * phase)
        y = y_coor + normal_amp2 * math.sin (phase + start_phase)
    else:
        x = x_coor + normal_amp1 * math.sin (phase + start_phase)
        y = y_coor + normal_amp2 * math.sin (phase / frequency_ratio)
    return x, y


x_center = (width_screen / 2) + 50
y_center = (height_screen / 2) + 50
f_r = f_a / f_b
n = 5000

# определение диапазона изменения фазы
if f_a == f_b:
    l = 2
else:
    l = lcm

# постороение кривой Лиссажу
for i in range(n):
    p = (i / n) * (l * math.pi)
    x, y = lissajous (x_center, y_center, a_norm, b_norm, f_r, p, phase)
    canvas.create_line (x, y, x + 1, y + 1, fill='green')




if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()

