import math

k=86399 #секунды
m=math.floor(k/60) #минуты для часов
h=math.floor(m/60) #часы
m1=m-(h*60) #минуты без часов
print("Прошло " + str(k) + " секунд")
print("Это " + str(h) + " часов и " + str(m1) + " минут")
