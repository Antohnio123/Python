import tkinter
import math
root = tkinter.Tk()
#   canvas.create_oval(x, y, x, y, width = 0, fill = 'white')  - рисование точки через овал
 #            canvas.create_line(x, y, x+1, y, fill="#ff0000")  - рисование точки через линию
 #   canvas.create_line(10, 10, 590, 590, fill="#ff0000")   #  просто рисуем линию
HEIGHT = 700
WIDTH = 700
MENUZONEHEIGHT = 100
MENUHEIGHT = 35
MENUWIDTH = 500
IndexK=1                 #   коэффициент для регулирования масштаба графика
Index=0.1      #   коэффициент для задания начального масштаба графика

# a*(k**s)+b*k+c - стандартная формула для графика
formula_a = "1"

# Задаем зону рисования ---------------------------
canvas = tkinter.Canvas (root, height = HEIGHT, width = WIDTH, bg = 'white')
canvas.pack()
# Координатные оси ---------------------------
def Coordinates():
    canvas.create_line(WIDTH/2,HEIGHT,WIDTH/2,0,width=1, arrow=tkinter.LAST, arrowshape="4 6 4")
    canvas.create_line(0,HEIGHT/2,WIDTH,HEIGHT/2,width=1, arrow=tkinter.LAST, arrowshape="4 6 4")
Coordinates()
# Задаем формулу рисования графика ---------------------------

def  Draw ():
    if formula_a.get()!="":     #   исключаем ошибку, вылезающую при попытке нарисовать график при остутствии формулы
        f = formula_a.get()
        f=f.replace('x', 'n')
        for i in range (0, WIDTH):
            x = i
            n=(x-WIDTH/2)*Index   #   умножение на Index тут приведёт к расширению или сужению графика по оси x
            try:    #  исключаем деление на ноль, рисовать эту точку всё равно не надо - она на оси y
                y = HEIGHT/2 - eval(f)/Index #   метод EVAL переводит string в выполняемое выражение.   Умножение на Index тут происходит, чтобы увеличить масштаб
         #   canvas.create_line(i, HEIGHT/2 - n, i+1, HEIGHT/2 - n, width=1, fill='black')  # - простая линия y = x для тестирования коэффициентов
                canvas.create_oval(x, int(y.real), x+1, int(y.real)+1, width = 1, fill = 'black')  # - сначала пришлось перевести в int float числа,  а потом методом .real ещё и отсечь комплексные
            except ZeroDivisionError:
                print ("Ошибка  деления на ноль при i =" + str(i))

def  Clear ():
    canvas.delete("all")  # Очищаем экран и снова рисуем координатные оси:
    Coordinates()
#------------------------------------------------------------------------------------------
def Scale():
    Index=scale.get()
    Index = 0.001 * IndexK    #   Почему метод не хочет видеть переменную Index из 13 строки, выражающую масштаб, но видит IndexK???????????????
    #   Почему нельзя на неё сослаться?  Вместо этого создаётся другой Index
    Clear()
    Draw()




# Выделяем зону под кнопки и место ввода ---------------------------
#frame1 = tkinter.Frame(root, bg = '#b3d9ff')
#frame1.pack (side='top', fill = 'both')
frame2 = tkinter.Frame(root, bg = 'gray', height=MENUZONEHEIGHT) # - серое поле внизу для кнопок и переключателей
frame2.pack(side='bottom', fill = 'x')
#frame2_1 = tkinter.Frame(frame2, bg = 'gray')
#frame2_1.pack(side='left', fill = 'both')
frameF = tkinter.Frame(frame2, bg = '#e6e6e6', width = MENUWIDTH, height = MENUHEIGHT) # - первый ряд: зона ввода формулы и 2 кнопок
frameF.place(y=MENUZONEHEIGHT/7, relx=0.05)
#frame2_2 = tkinter.Frame(frame2, bg = 'gray')
#frame2_2.pack(side='left', fill = 'both')
text1 = tkinter.Label (frameF, bg = '#e6e6e6', text=" Enter a formula using:\n '*'- multyplying, '**'- exponentiation ") # - текст слева от формулы
text1.pack(side='left')
text1 = tkinter.Label (frameF, bg = '#e6e6e6', text=" y(x) = ") # - текст второй слева от формулы
text1.pack(side='left')
formula_a = tkinter.Entry (frameF)   # - поле ввода формулы
formula_a.pack(side='left')
button = tkinter.Button (frameF, text="Draw", command = Draw)
button.pack(side='right')
buttonCS = tkinter.Button (frameF, text="Clear Screen", command = Clear)
buttonCS.pack(side='right')

frameS = tkinter.Frame(frame2, bg = '#e6e6e6', width = WIDTH, height = MENUHEIGHT)     # - второй ряд: зона настройки масштаба
frameS.place(y=MENUZONEHEIGHT/2, relx=0.05)
textS = tkinter.Label (frameS, bg = '#e6e6e6', text=" Scale: now 1 pixel is " + str(Index)+ "  ") # - текст слева от формулы
textS.pack(side='left')
buttonS = tkinter.Button (frameS, text="Change scale -->", command = Scale)
buttonS.pack(side='left')
scale = tkinter.Scale( frameS, orient=tkinter.HORIZONTAL, from_=1,to=1000, resolution = 10, variable =  Index )   # - вместо переменной ввёл метод, привязанный к этой переменной
scale.pack(side='right')





if tkinter._default_root:
    tkinter._default_root.update()
root.mainloop()
