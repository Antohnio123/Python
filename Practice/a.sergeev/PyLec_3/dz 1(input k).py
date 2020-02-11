import math

print ("Введите количество секунд")
k=int(input())
if k>=86400:
    m=int(math.floor(k/60)) #минуты для часов
    h=int((m//60)) #часы
    m1=int(m-(h*60)) #минуты без часов
    d=int(math.floor(h/24))
    h1=int(h-24*d)
    print("Прошло " + str(k) + " секунд")
    print("Это "  + str(d) + " суток, " + str(h1) + " часов и " + str(m1) + " минут")
else:
    m=int(math.floor(k/60)) #минуты для часов
    h=int((m//60)) #часы
    m1=int(m-(h*60)) #минуты без часов
    print("Прошло " + str(k) + " секунд")
    print("Это " + str(h) + " часов и " + str(m1) + " минут")
